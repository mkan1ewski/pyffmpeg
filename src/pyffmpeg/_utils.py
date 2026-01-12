from typing import Any, Iterable


def escape_chars(text: str, characters: str) -> str:
    """Escapes given characters in the text"""
    escape_set = set(characters)
    result = []
    for character in str(text):
        if character in escape_set:
            result.append(f"\\{character}")
        else:
            result.append(character)
    return "".join(result)


def escape_filter_option(text: str) -> str:
    """Escapes text on ffmpeg filter option level"""
    return escape_chars(text, ":='\\")


def escape_filter_description(text: str) -> str:
    """Escapes text on ffmpeg filter description level"""
    return escape_chars(text, "[],;'\\")


def escape_text_content(text: str) -> str:
    """Escapes text on ffmpeg text values level"""
    """Only needed for special filter options that are textual"""
    return escape_chars(text, "\\%'")


def convert_kwargs_to_cmd_line_args(
    kwargs: dict[str, Any], sort: bool = True
) -> list[str]:
    """
    Converts kwargs to list of args.
    """
    args = []
    options = sorted(kwargs.items()) if sort else kwargs.items()
    for key, value in options:
        if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
            for v in value:
                args.append(f"-{key}")
                if v is not None:
                    args.append(str(v))
        else:
            args.append(f"-{key}")
            if value is not None:
                args.append(str(value))
    return args


from pyffmpeg.node import Stream, FilterMultiOutput, FilterNode


def create_source(
    filter_name: str,
    positional_arguments: tuple = (),
    named_arguments: dict[str, Any] = {},
    num_outputs: int = 1,
    is_dynamic: bool = False,
) -> Stream | list[Stream] | FilterMultiOutput:
    """
    Internal factory for creating source filters.
    Handles single, multiple, and dynamic outputs.
    """
    node = FilterNode(
        filter_name=filter_name,
        positional_arguments=positional_arguments,
        named_arguments=named_arguments,
        inputs=[],
        num_output_streams=0 if is_dynamic else num_outputs,
    )

    if is_dynamic:
        return FilterMultiOutput(node)

    if num_outputs == 1:
        return node.output_streams[0]

    return node.output_streams
