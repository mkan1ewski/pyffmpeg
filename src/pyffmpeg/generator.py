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
        \"\"\"{{ description }}\"\"\"
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


def sanitize_parameter_name(name: str) -> str:
    """Secures against Python keywords (ex: 'class', 'import') hyphens and digits."""
    name = name.replace("-", "_")

    if keyword.iskeyword(name):
        return f"{name}_"

    if name and name[0].isdigit():
        return f"_{name}"

    return name


class CodeGenerator:
    def __init__(self, filter_data: dict[str, Any]):
        self.data = filter_data
        self.name = filter_data["filter_name"]
        self.description = filter_data.get("description", "")
        self.inputs = filter_data.get("inputs", [])
        self.options = filter_data.get("options", [])
        self.num_output_streams = len(filter_data.get("outputs", 1))
        self.is_dynamic_output = filter_data.get("is_dynamic_outputs", False)
        self.is_dynamic_inputs = filter_data.get("is_dynamic_inputs", False)

    def generate(self) -> str:
        """Generates full method code."""
        stream_parameters = self._get_stream_parameters()
        option_parameters = self._get_option_parameters()
        all_params = stream_parameters + option_parameters

        if self.is_dynamic_inputs:
            inputs_repr = "[self, *streams]"
        else:
            input_names = ["self"] + [
                sanitize_parameter_name(inp["name"]) for inp in self.inputs[1:]
            ]
            inputs_repr = f"[{', '.join(input_names)}]"

        if self.is_dynamic_output:
            method_name = "_apply_dynamic_outputs_filter"
            extra_args = ""
            return_suffix = ""
            return_type = '"FilterMultiOutput"'
        elif self.num_output_streams > 1:
            method_name = "_apply_filter"
            extra_args = f", num_output_streams={self.num_output_streams}"
            return_suffix = ""
            return_type = 'list["Stream"]'
        else:
            method_name = "_apply_filter"
            extra_args = ""
            return_suffix = "[0]"
            return_type = '"Stream"'

        processed_options = []
        for opt in self.options:
            processed_options.append(
                {
                    "ffmpeg_name": opt["name"],
                    "py_name": sanitize_parameter_name(opt["name"]),
                }
            )

        template = Template(METHOD_TEMPLATE)
        return template.render(
            name=self.name,
            params=all_params,
            return_type=return_type,
            description=self.description,
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
            default = self._get_default_value_repr(option)
            parameters.append(f"{name}: {type_hint} = {default}")
        return parameters

    def _get_type_hint(self, option: dict) -> str:
        """Creates a type hint."""
        base_type = TYPE_MAPPING.get(option["type"], "str")

        if option.get("choices"):
            literals = [f"'{choice['name']}'" for choice in option["choices"]]
            literal_str = f"Literal[{', '.join(literals)}]"

            if base_type == "int":
                return f"{literal_str} | int | None"
            return f"{literal_str} | None"

        return f"{base_type} | None"

    def _get_default_value_repr(self, option: dict) -> str:
        """Returns representation of default value in Python code"""
        # value = option.get("default")
        # option_type = option["type"]

        # if value is None:
        #     return "None"

        # C_CONSTANTS = {
        #     "INT_MAX", "INT_MIN", "UINT32_MAX",
        #     "INT64_MAX", "INT64_MIN", "I64_MIN", "I64_MAX",
        #     "DBL_MAX", "DBL_MIN", "FLT_MAX", "FLT_MIN",
        #     "NAN", "INFINITY"
        # }

        # # Jeśli wartość jest jedną z tych stałych -> ustawiamy None
        # if value in C_CONSTANTS:
        #     return "None"

        # if option_type == "boolean":
        #     return "True" if value == "true" else "False"

        # if option_type in ["string", "video_rate", "image_size", "color", "duration"]:
        #     return f'"{value}"'

        # if option_type in ["int", "float"]:
        #     if option.get("choices") and not value.replace(".", "", 1).isdigit():
        #         return f'"{value}"'
        #     return value

        # return f'"{value}"'
        return "None"
