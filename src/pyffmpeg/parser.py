from typing import Any
import re


class Parser:
    """Parses text output from 'ffmpeg --help filter=...' command."""

    def __init__(self, text: str) -> None:
        self.splitted_input: list[str] = text.splitlines()
        self.total_lines: int = len(self.splitted_input)
        self.current_index = 0
        self.line: str | None = None
        self.advance()
        self.filter_data = {}

    def advance(self) -> None:
        """Moves forward to the next line and buffers it."""
        if self.current_index == self.total_lines:
            self.line = None
            return
        self.line = self.splitted_input[self.current_index]
        self.current_index += 1

    def parse(self):
        """Orchestrates the parsing process."""
        if filter_name := self.parse_filter_name():
            self.filter_data["filter_name"] = filter_name
        if filter_description := self.parse_description():
            self.filter_data["description"] = filter_description
        self.filter_data["inputs"] = self.parse_inputs()
        self.filter_data["outputs"] = self.parse_outputs()
        if options := self.parse_options_block():
            self.filter_data["options"] = options
        return self.filter_data

    def parse_filter_name(self) -> str | None:
        """Scans the text for the 'Filter <name>' header"""
        while self.line is not None:
            if self.line.startswith("Filter "):
                parts = self.line.split()
                filter_name = parts[1]

                self.advance()
                return filter_name

            self.advance()

        return None

    def parse_description(self) -> str | None:
        """Gets filter description and skips to the next section"""
        description = None

        if self.line is not None and not self._is_section_header():
            description = self.line.strip()
            self.advance()

        while self.line is not None:
            if self._is_section_header():
                break
            self.advance()

        return description

    def parse_inputs(self) -> list[dict[str, str]]:
        """Parses the Inputs section."""
        inputs = []
        found_dynamic_keyword = False

        if self.line is None or self.line.strip() != "Inputs:":
            self.filter_data["is_dynamic_inputs"] = False
            return inputs

        self.advance()

        while self.line is not None:
            if self._is_section_header():
                break

            line = self.line.strip()

            if "none (source filter)" in line:
                self.advance()
                continue

            if "dynamic" in line.lower():
                found_dynamic_keyword = True
                self.advance()
                continue

            if line.startswith("#"):
                if input_data := self._parse_stream_line():
                    inputs.append(input_data)

            self.advance()

        if len(inputs) > 0:
            self.filter_data["is_dynamic_inputs"] = False
        else:
            self.filter_data["is_dynamic_inputs"] = found_dynamic_keyword

        return inputs

    def parse_outputs(self) -> list[dict[str, str]]:
        """Parses the Outputs section."""
        outputs = []
        found_dynamic_keyword = False

        if self.line is None or self.line.strip() != "Outputs:":
            return outputs
        self.advance()

        while self.line is not None:
            if self._is_section_header():
                break

            line = self.line.strip()

            if "none" in line.lower():
                self.advance()
                continue

            if "dynamic" in line.lower():
                found_dynamic_keyword = True
                self.advance()
                continue

            line = self.line.strip()
            if line.startswith("#"):
                if output_data := self._parse_stream_line():
                    outputs.append(output_data)

            self.advance()

        if len(outputs) > 0:
            self.filter_data["is_dynamic_outputs"] = False
        else:
            self.filter_data["is_dynamic_outputs"] = found_dynamic_keyword

        return outputs

    def _parse_stream_line(self) -> dict[str, str] | None:
        """
        Extracts name and type from line like: '#0: main (video)'
        Returns: {'name': 'main', 'type': 'video'} or None
        """
        parts = self.line.split(":")
        if len(parts) < 2:
            return None

        content = parts[1].strip()

        if "(" in content and content.endswith(")"):
            name_part, type_part = content.split("(", 1)
            return {"name": f"{name_part.strip()}_stream", "type": type_part.strip(")")}

        return None

    def parse_options_block(self) -> list[dict[str, Any]]:
        """Parses one block of AVOptions"""
        options = []
        if self.line is None or not self.line.strip().endswith("AVOptions:"):
            return options

        self.advance()

        while self.line is not None:
            stripped = self.line.strip()

            if self._is_section_header():
                break
            if not stripped:
                self.advance()
                continue

            parts = stripped.split(maxsplit=3)
            if len(parts) < 2:
                self.advance()
                continue

            name = parts[0]
            second_col = parts[1]
            raw_description = parts[3] if len(parts) > 3 else None

            if second_col.startswith("<") and second_col.endswith(">"):
                option_type = second_col[1:-1]

                description, default = self._extract_meta(raw_description)

                options.append(
                    {
                        "name": name,
                        "type": option_type,
                        "description": description,
                        "default": default,
                        "choices": [],
                    }
                )

            else:
                if options:
                    options[-1]["choices"].append(
                        {
                            "name": name,
                            "value": second_col,
                            "description": raw_description,
                        }
                    )
                else:
                    pass

            self.advance()

        return options

    def _extract_meta(self, text: str) -> tuple[str, str | None]:
        """Extracts description and default value."""
        if not text or "(default " not in text:
            return text, None

        description_part, value_part = text.rsplit("(default ", 1)
        raw_value = value_part.rsplit(")", 1)[0]
        default_val = raw_value.strip('"').strip()

        return description_part.strip(), default_val

    def _is_section_header(self) -> bool:
        """Checks if the line starts a new section."""
        if self.line is None:
            return False
        stripped = self.line.strip()
        return (
            stripped in ["Inputs:", "Outputs:"]
            or stripped.endswith("AVOptions:")
            or stripped.startswith("Exiting with")
            or stripped.startswith("This filter has support")
        )
