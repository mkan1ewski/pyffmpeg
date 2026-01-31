# Installation

## Prerequisites

Before installing pyffmpeg, ensure you have:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **FFmpeg available in your PATH**


## Installing pyffmpeg

### Using uv (Recommended)


```bash
uv add wut-ffmpeg
```

### Using pip

```bash
pip install wut-ffmpeg
```

### From Source

For development or the latest features:

```bash
git clone https://github.com/mkan1ewski/pyffmpeg.git
cd pyffmpeg
uv sync
```

## Verifying Installation

Test that everything is working:

```python
import pyffmpeg as ffmpeg

# Create a simple test
stream = ffmpeg.input('test.mp4')
args = stream.output('out.mp4').get_args()
print(args)
```

