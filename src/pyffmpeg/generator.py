from typing import Any


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

        stream_paramters = self._generate_stream_args()
        all_parameters = ", ".join(["self"] + stream_paramters)

        code = f"    def {self.name}({all_parameters}) -> Stream:\n"
        code += f'        """{self.description}"""\n'

        return code

    def _generate_stream_args(self) -> list[str]:
        """Generates parameters for additional input streams."""
        parameters = []
        # Skipping first input because it is self
        for input in self.inputs[1:]:
            sanitized_name = sanitize_parameter_name(input["name"])
            parameters.append(f"{sanitized_name}: Stream")
        return parameters
