# Quick Start

Get started with pyffmpeg in 5 minutes.

## Your First Pipeline

```python
import pyffmpeg as ffmpeg

# 1. Create an input
stream = ffmpeg.input('input.mp4')

# 2. Apply filters
stream = stream.filter('scale', w=1280, h=720)

# 3. Create output and run
stream.output('output.mp4').run()
```

## Common Tasks

### Resizing Video

```python
import pyffmpeg as ffmpeg

stream = ffmpeg.input('input.mp4')
stream = stream.scale(width=1920, height=1080)
stream.output('resized.mp4').run()
```

### Extracting Audio

```python
import pyffmpeg as ffmpeg

stream = ffmpeg.input('video.mp4')
audio = stream.audio
audio.output('audio.mp3').run()
```

### Converting Format

```python
import pyffmpeg as ffmpeg

ffmpeg.input('input.mp4').output('output.avi').run()
```

### Adding Watermark

```python
import pyffmpeg as ffmpeg

main = ffmpeg.input('video.mp4')
logo = ffmpeg.input('logo.png')

output = main.overlay(logo, x=10, y=10)
output.output('watermarked.mp4').run()
```

### Trimming Video

```python
import pyffmpeg as ffmpeg

# Trim from 00:00:10 to 00:00:30
stream = ffmpeg.input('input.mp4', ss='00:00:10', t=20)
stream.output('trimmed.mp4').run()
```

### Concatenating Videos

```python
import pyffmpeg as ffmpeg

# Create inputs
v1 = ffmpeg.input('part1.mp4')
v2 = ffmpeg.input('part2.mp4')
v3 = ffmpeg.input('part3.mp4')

# Concatenate
joined = ffmpeg.concat(v1, v2, v3)
joined.output('full_video.mp4').run()
```

## Method Chaining

One of pyffmpeg's strengths is fluent method chaining:

```python
import pyffmpeg as ffmpeg

(
    ffmpeg
    .input('input.mp4')
    .filter('scale', w=1280, h=720)
    .filter('fps', fps=30)
    .filter('hflip')  # Horizontal flip
    .output('output.mp4', vcodec='libx264', crf=23)
    .run()
)
```

## Working with Multiple Outputs

Process once, output to multiple files:

```python
import pyffmpeg as ffmpeg

input_stream = ffmpeg.input('input.mp4')

# Create multiple outputs
output1 = input_stream.output('720p.mp4', vcodec='libx264', s='1280x720')
output2 = input_stream.output('480p.mp4', vcodec='libx264', s='854x480')

# Run all at once
ffmpeg.merge_outputs(output1, output2).run()
```

## Checking the Command

Before running, you can inspect the generated FFmpeg command:

```python
import pyffmpeg as ffmpeg

stream = ffmpeg.input('input.mp4')
stream = stream.scale(width=1280, height=720)
output = stream.output('output.mp4')

# Get the command arguments
args = output.get_args()
print(' '.join(args))
# Output: -i input.mp4 -filter_complex [0]scale=w=1280:h=720[s0] -map [s0] output.mp4
```

## Async Execution

For long-running operations, use async execution:

```python
import pyffmpeg as ffmpeg

stream = ffmpeg.input('large_video.mp4')
output = stream.output('compressed.mp4')

# Start process without blocking
process = output.run_async()

# Do other work...
print("Processing video in background...")

# Wait for completion
process.wait()
print("Done!")
```

