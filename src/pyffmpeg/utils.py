import re
import subprocess
from typing import Sequence

from pyffmpeg.node import (
    InputNode,
    OutputNode,
    Stream,
    MergedOutputNode,
    GraphSorter,
    CommandBuilder,
)


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


def unify_names(all_names):
    for i, names in enumerate(all_names):  # iterate through outer list
        for j, name in enumerate(names):  # iterate through inner list
            # modify the string and assign it back to the same position
            all_names[i][j] = (
                name.replace("(", "")
                .replace(")", "")
                .replace("/", "_")
                .replace("|", "")
            )


def unify_keys(all_options):
    for i, options_list in enumerate(all_options):
        for j, d in enumerate(options_list):
            new_dict = {}
            for key, value in d.items():
                # Replace hyphen with underscore in the key
                new_key = key.replace("-", "_").replace(">", "_").replace("+", "_")
                if new_key in [
                    "pass",
                    "and",
                    "lambda",
                    "class",
                    "in",
                    "or",
                    "if",
                    "raise",
                    "as",
                ]:
                    new_key += "_"
                if new_key[0].isdigit():
                    new_key = "_" + new_key
                new_dict[new_key] = value
            all_options[i][j] = new_dict


def input(path: str, **kwargs) -> Stream:
    """Creates input stream from a filename"""
    """Accepts input options through kwargs"""
    return InputNode(path, kwargs).output_streams[0]


def merge_outputs(*outputs: OutputNode) -> MergedOutputNode:
    """Creates multioutput object from many outputs"""
    return MergedOutputNode(outputs)


def get_args(
    output: OutputNode | Sequence[OutputNode] | MergedOutputNode, **global_options
) -> list[str]:
    """Creates command arguments for the output or a list of outputs"""
    if isinstance(output, Sequence):
        # output is reversed to satisfy tests order requirements
        output = MergedOutputNode(outputs=tuple(reversed(output)))
    sorter = GraphSorter(output)
    command_builder = CommandBuilder(
        sorter.sort(),
        output.global_options + output._compile_global_kwargs(global_options),
    )
    return command_builder.build_args()


def filter(self, filter_name: str, inputs: list["Stream"], **kwargs) -> "Stream":
    """Custom filter with single or many inputs and a single output"""
    if inputs and isinstance(inputs[0], Stream):
        return inputs[0].filter(filter_name, inputs, **kwargs)
