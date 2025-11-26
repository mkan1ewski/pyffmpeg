from pyffmpeg.node import RunnableNode, OutputNode, MergedOutputNode


def compile(
    node: RunnableNode,
    cmd: str = "ffmpeg",
    overwrite_output: bool = False,
    **global_options,
) -> list[str]:
    return node.compile(cmd=cmd, overwrite_output=overwrite_output, **global_options)


def run(
    node_or_node_list: RunnableNode | list[OutputNode],
    cmd: str | list[str] = "ffmpeg",
    capture_stdout: bool = False,
    capture_stderr: bool = False,
    input: bytes | None = None,
    quiet: bool = False,
    overwrite_output: bool = False,
    cwd: str | None = None,
) -> tuple[bytes | None, bytes | None]:
    """Executes ffmpeg command."""
    if isinstance(node_or_node_list, (list, tuple)) and all(
        [isinstance(n, OutputNode) for n in node_or_node_list]
    ):
        node_or_node_list = MergedOutputNode(node_or_node_list)
    return node_or_node_list.run(
        cmd=cmd,
        capture_stdout=capture_stdout,
        capture_stderr=capture_stderr,
        input=input,
        quiet=quiet,
        overwrite_output=overwrite_output,
        cwd=cwd,
        compile_function=compile,
    )
