import pyffmpeg as ffmpeg

stream1, stream2 = ffmpeg.input("video.mp4").vflip().split()
print(stream1.hflip().overlay(stream2).ocr().output("a").compile())
