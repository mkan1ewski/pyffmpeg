import re
import subprocess


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


def preprocess_code(filename) -> str | None:
    """Preprocesses a C file using clang."""
    result = subprocess.run(
        [
            "clang",
            "-E",
            "-D__attribute__(x)=",
            "-D__extension__=",
            "-I",
            "./pycparser/utils/fake_libc_include",
            "-I",
            "./FFmpeg",
            "-I",
            "./FFmpeg/libavcodec/",
            f"./FFmpeg/libavfilter/{filename}",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        preprocessed_code = result.stdout
        return preprocessed_code
    else:
        return None
