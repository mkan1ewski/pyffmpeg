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
