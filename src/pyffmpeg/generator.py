from jinja2 import Template
from typing import Any
import keyword

TYPE_MAPPING = {
    "int": "int",
    "float": "float",
    "double": "float",
    "boolean": "bool",
    "string": "str",
    "video_rate": "str",
    "image_size": "str",
    "duration": "str",
    "color": "str",
    "rational": "str",
    "flags": "str",
}

METHOD_TEMPLATE = """
    def {{ name }}(self, {{ params|join(', ') }}) -> {{ return_type }}:
        \"\"\"{{ description }}

        {%- if input_docs or option_docs %}

        Args:
            {%- for inp in input_docs %}
            {{ inp.name }} ({{ inp.type }}): {{ inp.help }}
            {%- endfor %}
            {%- for opt in option_docs %}
            {{ opt.name }} ({{ opt.type }}): {{ opt.help }}
                {% if opt.choices %}
                Allowed values:
                    {%- for choice in opt.choices %}
                    {%- if choice.desc %}
                    * {{ choice.name }}: {{ choice.desc }}
                    {%- else %}
                    * {{ choice.name }}
                    {%- endif %}
                    {%- endfor %}
                {% endif %}
                {%- if opt.default and opt.default != "None" %}
                Defaults to {{ opt.default }}.
                {%- endif %}
            {%- endfor %}
        {%- endif %}

        Returns:
            {{ return_type }}: {{ return_help }}
        \"\"\"
        return self.{{ method_name }}(
            filter_name="{{ filter_name }}",
            inputs={{ inputs_repr }},
            named_arguments={
                {%- for opt in options %}
                "{{ opt.ffmpeg_name }}": {{ opt.py_name }},
                {%- endfor %}
            }{{ extra_args }}
        ){{ return_suffix }}
"""

SOURCE_TEMPLATE = """
def {{ name }}({{ params|join(', ') }}) -> {{ return_type }}:
    \"\"\"{{ description }}

    {%- if option_docs %}
    Args:
        {%- for opt in option_docs %}
        {{ opt.name }} ({{ opt.type }}): {{ opt.help }}
            {% if opt.choices %}
            Allowed values:
                {%- for choice in opt.choices %}
                * {{ choice.name }}
                {%- endfor %}
            {% endif %}
            {%- if opt.default and opt.default != "None" %}
            Defaults to {{ opt.default }}.
            {%- endif %}
        {%- endfor %}
    {%- endif %}

    Returns:
        {{ return_type }}: {{ return_help }}
    \"\"\"
    return create_source(
        filter_name="{{ filter_name }}",
        named_arguments={
            {%- for opt in options %}
            "{{ opt.ffmpeg_name }}": {{ opt.py_name }},
            {%- endfor %}
        }{{ extra_args }}
    )
"""


def sanitize_parameter_name(name: str) -> str:
    """Secures against Python keywords (ex: 'class', 'import') hyphens and digits."""
    name = name.replace("-", "_")

    if keyword.iskeyword(name):
        return f"{name}_"

    if name and name[0].isdigit():
        return f"_{name}"

    return name


class CodeGenerator:
    def __init__(self, filter_data: dict[str, Any], is_source: bool = False):
        self.data = filter_data
        self.is_source = is_source
        self.name = filter_data["filter_name"]
        self.description = filter_data.get("description", "").replace("\n", " ").strip()
        self.inputs = filter_data.get("inputs", [])
        self.options = filter_data.get("options", [])
        self.num_output_streams = len(filter_data.get("outputs", 1))
        self.is_dynamic_output = filter_data.get("is_dynamic_outputs", False)
        self.is_dynamic_inputs = filter_data.get("is_dynamic_inputs", False)

    def generate(self) -> str:
        """Generates full method code."""
        option_parameters = self._get_option_parameters()
        option_docs = self._get_option_docs()

        processed_options = []
        for opt in self.options:
            processed_options.append(
                {
                    "ffmpeg_name": opt["name"],
                    "py_name": sanitize_parameter_name(opt["name"]),
                }
            )

        return_help, return_type, return_suffix = self._get_return_info()
        method_name, extra_args, inputs_repr = self._get_body_info()

        if self.is_source:
            extra_args_list = []
            if self.is_dynamic_output:
                extra_args_list.append("is_dynamic=True")
            elif self.num_output_streams != 1:
                extra_args_list.append(f"num_outputs={self.num_output_streams}")

            extra_args_str = ", ".join(extra_args_list)
            if extra_args_str:
                extra_args_str = f", {extra_args_str}"

            template = Template(SOURCE_TEMPLATE)
            return template.render(
                name=self.name,
                params=option_parameters,
                return_type=return_type,
                description=self.description,
                option_docs=option_docs,
                return_help=return_help,
                filter_name=self.name,
                options=processed_options,
                extra_args=extra_args_str,
            )
        else:
            stream_parameters = self._get_stream_parameters()
            input_docs = self._get_input_docs()

            all_params = stream_parameters + option_parameters

            template = Template(METHOD_TEMPLATE)
            return template.render(
                name=self.name,
                params=all_params,
                return_type=return_type,
                description=self.description,
                input_docs=input_docs,
                option_docs=option_docs,
                return_help=return_help,
                method_name=method_name,
                filter_name=self.name,
                inputs_repr=inputs_repr,
                options=processed_options,
                extra_args=extra_args,
                return_suffix=return_suffix,
            )

    def _get_stream_parameters(self) -> list[str]:
        """Generates parameters for additional input streams."""
        if self.is_dynamic_inputs:
            return ['*streams: "Stream"']
        # skipping first because it will be self
        return [
            f'{sanitize_parameter_name(inp["name"])}: "Stream"'
            for inp in self.inputs[1:]
        ]

    def _get_option_parameters(self) -> list[str]:
        """Generates parameters for options (x, y, eof_action)."""
        parameters = []
        for option in self.options:
            name = sanitize_parameter_name(option["name"])
            type_hint = self._get_type_hint(option)
            parameters.append(f"{name}: {type_hint} = None")
        return parameters

    def _get_body_info(self) -> tuple[str, str, str]:
        """
        Determines the details for the internal method call body.

        Returns:
            tuple[str, str, str]: A tuple containing:
                - method_name: Name of the internal method to call (e.g. '_apply_filter').
                - extra_args: Additional arguments string (e.g. ', num_output_streams=2').
                - inputs_repr: String representation of the inputs list (e.g. '[self, *streams]').
        """
        if self.is_dynamic_inputs:
            inputs_repr = "[self, *streams]"
        else:
            input_names = ["self"] + [
                sanitize_parameter_name(inp["name"]) for inp in self.inputs[1:]
            ]
            inputs_repr = f"[{', '.join(input_names)}]"

        if self.is_dynamic_output:
            return "_apply_dynamic_outputs_filter", "", inputs_repr
        elif self.num_output_streams > 1:
            return (
                "_apply_filter",
                f", num_output_streams={self.num_output_streams}",
                inputs_repr,
            )
        elif self.num_output_streams == 0:
            return "_apply_sink_filter", "", inputs_repr
        else:
            return "_apply_filter", "", inputs_repr

    def _get_return_info(self) -> tuple[str, str, str]:
        """
        Determines return type information for the generated method.

        Returns:
            tuple[str, str, str]: A tuple containing:
                - return_help: Description for the docstring Returns section.
                - return_type: Python type hint string (e.g. '"Stream"').
                - return_suffix: Suffix to append to the internal method call (e.g. '[0]' or '').
        """
        if self.is_dynamic_output:
            return (
                "A FilterMultiOutput object to access dynamic outputs.",
                '"FilterMultiOutput"',
                "",
            )
        elif self.num_output_streams > 1:
            return (
                f"A list of {self.num_output_streams} Stream objects.",
                'list["Stream"]',
                "",
            )
        elif self.num_output_streams == 0:
            return (
                "A SinkNode representing the sink (terminal node).",
                '"SinkNode"',
                "",
            )
        else:
            return "The output stream.", '"Stream"', "[0]"

    def _get_input_docs(self) -> list[dict[str, str]]:
        docs = []
        if self.is_dynamic_inputs:
            docs.append(
                {
                    "name": "*streams",
                    "type": "Stream",
                    "help": "One or more input streams.",
                }
            )
        else:
            for inp in self.inputs[1:]:
                raw_type = inp.get("type", "Stream")
                docs.append(
                    {
                        "name": sanitize_parameter_name(inp["name"]),
                        "type": "Stream",
                        "help": f"Input {raw_type} stream.",
                    }
                )
        return docs

    def _get_option_docs(self) -> list[dict[str, Any]]:
        docs = []
        for option in self.options:
            raw_help = option.get("description") or "No description available."
            clean_help = raw_help.replace("\n", " ").strip()
            base_type = TYPE_MAPPING.get(option.get("type"), "str")

            if option.get("choices") and base_type == "int":
                doc_type = "int | str"
            else:
                doc_type = base_type

            choices_doc = []
            if option.get("choices"):
                for choice in option["choices"]:
                    desc = choice.get("description") or ""
                    clean_desc = desc.replace("\n", " ").strip()
                    choices_doc.append({"name": choice["name"], "desc": clean_desc})

            raw_default = option.get("default")
            if raw_default is None or raw_default == "" or raw_default == "None":
                default_val = None
            else:
                default_val = str(raw_default).strip('"')

            docs.append(
                {
                    "name": sanitize_parameter_name(option["name"]),
                    "type": doc_type,
                    "help": clean_help,
                    "choices": choices_doc,
                    "default": default_val,
                }
            )
        return docs

    def _get_type_hint(self, option: dict) -> str:
        """Creates a type hint for function signature."""
        base_type = TYPE_MAPPING.get(option["type"], "str")

        if option.get("choices"):
            literals = [f"'{choice['name']}'" for choice in option["choices"]]
            literal_str = f"Literal[{', '.join(literals)}]"

            if base_type == "int":
                return f"{literal_str} | int | None"
            return f"{literal_str} | None"

        return f"{base_type} | None"

    def _get_default_value_repr(self, option: dict) -> str:
        """Returns representation of default value in Python code - NOT USED in docs, only for logical defaults if needed"""
        return "None"
