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


def get_c_files_names(object_files: list[str]) -> list[str]:
    """Changes object file names to equivalent .c file names."""
    return [file[:-1] + "c" for file in object_files]
