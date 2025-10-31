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
