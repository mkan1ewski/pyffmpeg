import pytest


@pytest.fixture(params=["NEW", "COMPAT"])
def ffmpeg_module(request):
    if request.param == "COMPAT":
        import pyffmpeg._compat as ffmpeg

        return ffmpeg
    elif request.param == "NEW":
        import pyffmpeg as ffmpeg

        return ffmpeg
    else:
        raise NotImplementedError(request.param)
