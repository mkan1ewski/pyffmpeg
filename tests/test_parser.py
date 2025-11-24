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


def test_scale_description():
    data = get_parsed_filter_data("scale")
    assert data.get("inputs") == [{"name": "default", "type": "video"}]
