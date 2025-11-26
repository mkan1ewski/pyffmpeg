import subprocess
from typing import Any
import pytest
from pyffmpeg.parser import Parser


def get_parsed_filter_data(filter_name: str) -> dict[str, Any]:
    """Runs ffmpeg help for a given filter, parses output and returns data"""
    cmd = ["ffmpeg", "--help", f"filter={filter_name}"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0

    parser = Parser(result.stdout)
    return parser.parse()


def test_overlay_filter_name():
    data = get_parsed_filter_data("overlay")
    assert data.get("filter_name") == "overlay"


def test_scale_filter_name():
    data = get_parsed_filter_data("scale")
    assert data.get("filter_name") == "scale"


def test_overlay_description():
    data = get_parsed_filter_data("overlay")
    assert data.get("description") == "Overlay a video source on top of the input."


def test_scale_description():
    data = get_parsed_filter_data("scale")
    assert (
        data.get("description")
        == "Scale the input video size and/or convert the image format."
    )


def test_overlay_inputs():
    data = get_parsed_filter_data("overlay")
    assert data.get("inputs") == [
        {"name": "main", "type": "video"},
        {"name": "overlay", "type": "video"},
    ]


def test_scale_inputs():
    data = get_parsed_filter_data("scale")
    assert data.get("inputs") == [{"name": "default", "type": "video"}]


def test_overlay_outputs():
    data = get_parsed_filter_data("overlay")
    assert data.get("outputs") == [{"name": "default", "type": "video"}]


def test_scale_outputs():
    data = get_parsed_filter_data("scale")
    assert data.get("outputs") == [{"name": "default", "type": "video"}]


def test_split_outputs():
    data = get_parsed_filter_data("split")
    print(data)
    assert data.get("outputs") == None


def test_overlay_option_block():
    data = get_parsed_filter_data("overlay")
    assert data["options"][0] == {
        "name": "x",
        "type": "string",
        "description": "set the x expression",
        "default": "0",
        "choices": [],
    }
    assert data["options"][2] == {
        "name": "eof_action",
        "type": "int",
        "description": "Action to take when encountering EOF from secondary input  (from 0 to 2)",
        "default": "repeat",
        "choices": [
            {
                "name": "repeat",
                "value": "0",
                "description": "Repeat the previous frame.",
            },
            {"name": "endall", "value": "1", "description": "End both streams."},
            {
                "name": "pass",
                "value": "2",
                "description": "Pass through the main input.",
            },
        ],
    }
