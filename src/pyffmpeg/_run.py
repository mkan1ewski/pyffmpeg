import subprocess
from pyffmpeg.node import RunnableNode


def compile(
    node: RunnableNode,
    cmd: str = "ffmpeg",
    overwrite_output: bool = False,
    **global_options,
) -> list[str]:
    return node.compile(cmd=cmd, overwrite_output=overwrite_output, **global_options)


def run(
    node: RunnableNode,
    cmd: str | list[str] = "ffmpeg",
    capture_stdout: bool = False,
    capture_stderr: bool = False,
    input: bytes | None = None,
    quiet: bool = False,
    overwrite_output: bool = False,
    cwd: str | None = None,
) -> tuple[bytes | None, bytes | None]:
    return node.run(
        cmd=cmd,
        capture_stdout=capture_stdout,
        capture_stderr=capture_stderr,
        input=input,
        quiet=quiet,
        overwrite_output=overwrite_output,
        cwd=cwd,
        compile_function=compile,
    )


def run_async(
    node: RunnableNode,
    cmd: str | list[str] = "ffmpeg",
    pipe_stdin: bool = False,
    pipe_stdout: bool = False,
    pipe_stderr: bool = False,
    input: bytes | None = None,
    quiet: bool = False,
    overwrite_output: bool = False,
    cwd: str | None = None,
) -> subprocess.Popen:
    """Runs ffmpeg process asynchronously"""
    args = compile(node, cmd, overwrite_output=overwrite_output)
    stdin_stream = subprocess.PIPE if pipe_stdin else None
    stdout_stream = subprocess.PIPE if pipe_stdout else None
    stderr_stream = subprocess.PIPE if pipe_stderr else None
    if quiet:
        stderr_stream = subprocess.STDOUT
        stdout_stream = subprocess.DEVNULL
    return subprocess.Popen(
        args,
        stdin=stdin_stream,
        stdout=stdout_stream,
        stderr=stderr_stream,
        cwd=cwd,
    )
