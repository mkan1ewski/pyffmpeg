import subprocess
import json
from typing import Any
from pyffmpeg.errors import Error
from pyffmpeg._utils import convert_kwargs_to_cmd_line_args


def probe(
    filename: str, cmd: str = "ffprobe", timeout: float | None = None, **kwargs
) -> dict[str, Any]:
    """
    Runs ffprobe and returns parsed json result
    """
    options = ["-show_format", "-show_streams", "-of", "json"]
    options.extend(convert_kwargs_to_cmd_line_args(kwargs))
    args = [cmd, *options, filename]
    result = subprocess.run(args, capture_output=True, timeout=timeout, check=False)

    if result.returncode != 0:
        raise Error(
            "ffprobe error (see stderr output for detail)", result.stdout, result.stderr
        )

    return json.loads(result.stdout)
