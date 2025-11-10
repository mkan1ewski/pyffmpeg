class Error(Exception):
    """Error running ffmpeg process"""

    def __init__(self, message, stdout=None, stderr=None):
        super().__init__(message)
        self.stdout = stdout
        self.stderr = stderr
