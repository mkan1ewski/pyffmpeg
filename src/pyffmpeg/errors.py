class Error(Exception):
    """Error raised when running an ffmpeg process"""

    def __init__(
        self,
        message: str,
        stdout: bytes | None = None,
        stderr: bytes | None = None,
    ) -> None:
        super().__init__(message)
        self.stdout: bytes | None = stdout
        self.stderr: bytes | None = stderr
