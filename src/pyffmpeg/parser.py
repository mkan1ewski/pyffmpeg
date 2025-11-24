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
        if filter_inputs := self.parse_inputs():
            self.filter_data["inputs"] = filter_inputs
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

        if self.line is None or self.line.strip() != "Inputs:":
            return inputs
        self.advance()

        while self.line is not None:
            if self._is_section_header():
                break

            line = self.line.strip()
            if line.startswith("#"):
                if input_data := self._parse_stream_line():
                    inputs.append(input_data)

            self.advance()

        return inputs

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
            return {"name": name_part.strip(), "type": type_part.strip(")")}

        return None

    def _is_section_header(self) -> bool:
        """Checks if the line starts a new section."""
        if self.line is None:
            return False
        stripped = self.line.strip()
        return stripped in ["Inputs:", "Outputs:"] or stripped.endswith("AVOptions:")
