import sys
import os

# Add a specific folder
dirname = os.path.dirname(__file__)
project_path = os.path.join(dirname, "../..")
sys.path.append(project_path)
from pyffmpeg.utils import (
    extract_filenames,
    get_c_files_names,
    preprocess_code,
    unify_names,
    unify_keys,
)
from pycparser.pycparser.plyparser import ParseError
from pycparser.pycparser import c_parser
from pyffmpeg.ast_visitor import FilterVisitor


c_files = get_c_files_names(extract_filenames("FFmpeg/libavfilter/Makefile"))
parser = c_parser.CParser()

all_names = []
all_options = []
all_inputs = []
all_outputs = []
print("Processing files:", c_files)
for c_file in c_files:
    preprocessed_code = preprocess_code(c_file)
    if preprocessed_code is None:
        print(f"Failed to preprocess {c_file}.")
        continue
    try:
        ast = parser.parse(preprocessed_code)
    except ParseError as e:
        print(f"Parse error in {c_file}: {e}")
        continue

    visitor = FilterVisitor()
    visitor.visit(ast)
    all_names.append(visitor.filter_names)
    all_options.append(visitor.filter_options)
    all_inputs.append(visitor.filter_inputs)
    all_outputs.append(visitor.filter_outputs)

# print("Filter names:", all_names)
# print("Filter options:", all_options)
# print(len(all_names), "filter names found.")
# print(len(all_options), "filter options found.")
unify_names(all_names)
print(all_options)
unify_keys(all_options)

for i, names in enumerate(all_names):
    if len(names) != len(all_inputs[i]):
        all_inputs[i] = [1 for _ in range(len(names))]

    if len(names) != len(all_outputs[i]):
        all_outputs[i] = [1 for _ in range(len(names))]

with open("defs.py", "w") as f:
    for names, options, inputs, outputs in zip(
        all_names, all_options, all_inputs, all_outputs
    ):
        for name, opts, inputs_count, outputs_count in zip(
            names, options, inputs, outputs
        ):
            str = f"""def {name}(self, {", ".join(opts.keys())}):
        return self._apply_filter("{name}", locals()){"[0]" if outputs_count == 1 else ""}
"""
            f.write(str)
