import textwrap
from typing import Any

TYPE_MAPPING = {
    "int": "int",
    "float": "float",
    "boolean": "bool",
    "string": "str",
    "video_rate": "str",
    "image_size": "str",
    "duration": "str",
    "color": "str",
    "rational": "str",
    "flags": "str",
}


def sanitize_parameter_name(name: str) -> str:
    """Secures against Python keywords (ex: 'class', 'import') and hyphens."""
    KEYWORDS = {
        "class",
        "import",
        "return",
        "pass",
        "from",
        "global",
        "with",
        "async",
        "await",
        "def",
        "lambda",
    }
    if name in KEYWORDS:
        return f"{name}_"
    return name.replace("-", "_")


class CodeGenerator:
    def __init__(self, filter_data: dict[str, Any]):
        self.data = filter_data
        self.name = filter_data["filter_name"]
        self.description = filter_data.get("description", "")
        self.inputs = filter_data.get("inputs", [])
        self.options = filter_data.get("options", [])

    def generate(self) -> str:
        """Generates full method code."""

        stream_parameters = self._generate_stream_parameters()
        option_parameters = self._generate_option_parameters()

        all_parameters = ", ".join(["self"] + stream_parameters + option_parameters)

        body = self._generate_body()

        return f"""
    def {self.name}({all_parameters}) -> "Stream":
        \"\"\"{self.description}\"\"\"
{body}
"""

    def _generate_stream_parameters(self) -> list[str]:
        """Generates parameters for additional input streams."""
        if self.data.get("is_dynamic_inputs", False):
            return ['*streams: "Stream"']

        parameters = []
        # Skipping first input because it is self
        for input in self.inputs[1:]:
            sanitized_name = sanitize_parameter_name(input["name"])
            parameters.append(f'{sanitized_name}: "Stream"')
        return parameters

    def _generate_option_parameters(self) -> list[str]:
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
                return f"{literal_str} | int"
            return literal_str

        return base_type

    def _get_default_value_repr(self, option: dict) -> str:
        """Returns representation of default value in Python code"""
        value = option.get("default")
        option_type = option["type"]

        if value is None:
            return "None"

        if option_type == "boolean":
            return "True" if value == "true" else "False"

        if option_type in ["string", "video_rate", "image_size", "color", "duration"]:
            return f'"{value}"'

        if option_type in ["int", "float"]:
            if option.get("choices") and not value.replace(".", "", 1).isdigit():
                return f'"{value}"'
            return value

        return f'"{value}"'

    def _generate_body(self) -> str:
        """Generates body of the method."""
        is_dynamic_inputs = self.data.get("is_dynamic_inputs", False)
        if is_dynamic_inputs:
            inputs_list_as_str = "[self, *streams]"
        else:
            inputs_list = ["self"] + [
                sanitize_parameter_name(inp["name"]) for inp in self.inputs[1:]
            ]
            inputs_list_as_str = f"[{', '.join(inputs_list)}]"

        named_arguments_entries = []
        for option in self.options:
            py_name = sanitize_parameter_name(option["name"])
            ffmpeg_name = option["name"]
            named_arguments_entries.append(f'"{ffmpeg_name}": {py_name},')

        named_arguments_dict = "\n".join(named_arguments_entries)

        raw_body = f"""
return self._apply_filter(
    filter_name="{self.name}",
    inputs={inputs_list_as_str},
    named_arguments={{
{textwrap.indent(named_arguments_dict, 8 * " ")}
    }}
)[0]
"""
        return textwrap.indent(raw_body.strip(), 8 * " ")
