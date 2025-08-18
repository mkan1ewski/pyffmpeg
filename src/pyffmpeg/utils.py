import re


def extract_filenames(makefile: str = "Makefile") -> list[str]:
    """Extracts filenames defining filters from a Makefile."""
    filenames = []
    with open(makefile) as f:
        for line in f:
            match = re.search(r"FILTER\)\s*\+=\s*([^\s]+)", line)
            if match:
                filenames.append(match.group(1))
    return filenames
