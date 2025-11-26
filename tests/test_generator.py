from tests.test_parser import get_parsed_filter_data
from pyffmpeg.generator import CodeGenerator
from pprint import pprint


def get_generated_method(filter_name: str) -> str:
    filter_data = get_parsed_filter_data(filter_name)

    code_generator = CodeGenerator(filter_data)
    return code_generator.generate()


def test_split_code_streams():
    method_code = get_generated_method("split")
    assert "    def split(self)" in method_code


def test_overlay_code_streams():
    method_code = get_generated_method("overlay")
    assert "    def overlay(self, overlay: Stream)" in method_code
