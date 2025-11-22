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


def convert_kwargs_to_cmd_line_args(kwargs: dict[str, Any]) -> list[str]:
    """
    Converts kwargs to list of args.
    """
    args = []
    for key, value in sorted(kwargs.items()):
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


#
