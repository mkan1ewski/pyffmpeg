from pyffmpeg._utils import (
    escape_filter_option,
    escape_filter_description,
    escape_text_content,
    convert_kwargs_to_cmd_line_args,
)
from pyffmpeg.generated_filters import GeneratedFiltersMixin
from pyffmpeg.errors import Error
from typing import Any, Sequence
import subprocess


class Node:
    """Abstract base class for all components in the FFmpeg processing graph."""


class ProcessableNode(Node):
    """Nodes that can be further processed with filters."""

    def __init__(self, num_output_streams: int = 1):
        self.output_streams: list[Stream] = [
            Stream(self) for i in range(num_output_streams)
        ]


class RunnableNode(Node):
    def __init__(self):
        self.global_options: list[str] = []

    def global_args(self, *args) -> "RunnableNode":
        """Adds global options"""
        self.global_options.extend(args)
        return self

    def overwrite_output(self) -> "RunnableNode":
        """Adds global overwrite option"""
        self.global_options.append("-y")
        return self

    def _compile_global_kwargs(self, options_dict: dict) -> list[str]:
        """Converts kwargs to list"""
        args = []
        key_map = {
            "overwrite_output": "y",
            "log_level": "loglevel",
            "quiet": "loglevel",
        }
        for key, value in options_dict.items():
            if key == "quiet" and value is True:
                args.extend(["-loglevel", "quiet"])
                continue

            flag_name = key_map.get(key, key)

            if value is True:
                # -y with overwrite_output=True
                args.append(f"-{flag_name}")
            elif value is not None and value is not False:
                # handles for example log_level="error"
                args.extend([f"-{flag_name}", str(value)])
        return args

    def get_args(self, overwrite_output=False, **global_options) -> list[str]:
        """Builds command arguments"""
        global_options["overwrite_output"] = overwrite_output
        kwargs_args = self._compile_global_kwargs(global_options)
        sorter = GraphSorter(self)
        command_builder = CommandBuilder(
            sorter.sort(), self.global_options + kwargs_args
        )
        return command_builder.build_args()

    def compile(
        self, cmd: str = "ffmpeg", overwrite_output: bool = False, **global_options
    ) -> list[str]:
        """Builds command line arguments for invoking ffmpeg"""
        if isinstance(cmd, str):
            cmd = [cmd]
        elif not isinstance(cmd, list):
            cmd = list(cmd)
        return cmd + self.get_args(overwrite_output=overwrite_output, **global_options)

    def run(
        self,
        cmd: str | list[str] = "ffmpeg",
        capture_stdout: bool = False,
        capture_stderr: bool = False,
        input: bytes | None = None,
        quiet: bool = False,
        overwrite_output: bool = False,
        cwd: str | None = None,
        compile_function=None,
    ) -> tuple[bytes | None, bytes | None]:
        """Execute the ffmpeg command represented by a RunnableNode"""
        if not isinstance(self, RunnableNode):
            raise TypeError(f"Expected RunnableNode, got {type(self)}")

        compile_function = compile_function or self.__class__.compile
        cmdline = compile_function(
            self,
            cmd=cmd,
            overwrite_output=overwrite_output,
            quiet=quiet,
        )

        stdout = subprocess.PIPE if capture_stdout else None
        stderr = subprocess.PIPE if capture_stderr else None

        try:
            process = subprocess.run(
                cmdline,
                input=input,
                stdout=stdout,
                stderr=stderr,
                cwd=cwd,
                check=True,
            )
            return process.stdout, process.stderr
        except subprocess.CalledProcessError as e:
            raise Error(
                "ffmpeg error (see stderr output for detail)",
                stdout=e.stdout,
                stderr=e.stderr,
            )

    def run_async(
        self,
        cmd: str | list[str] = "ffmpeg",
        pipe_stdin: bool = False,
        pipe_stdout: bool = False,
        pipe_stderr: bool = False,
        input: bytes | None = None,
        quiet: bool = False,
        overwrite_output: bool = False,
        cwd: str | None = None,
    ) -> subprocess.Popen:
        """Runs ffmpeg process asynchronously"""
        args = self.compile(cmd, overwrite_output=overwrite_output)
        stdin_stream = subprocess.PIPE if pipe_stdin else None
        stdout_stream = subprocess.PIPE if pipe_stdout else None
        stderr_stream = subprocess.PIPE if pipe_stderr else None
        if quiet:
            stderr_stream = subprocess.STDOUT
            stdout_stream = subprocess.DEVNULL
        return subprocess.Popen(
            args,
            stdin=stdin_stream,
            stdout=stdout_stream,
            stderr=stderr_stream,
            cwd=cwd,
        )


class InputNode(ProcessableNode):
    """Nodes representing input files."""

    def __init__(self, filename: str, options: dict[str, Any] = None):
        super().__init__()
        self.filename: str = filename
        self.options: dict[str, Any] = options

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, InputNode):
            return NotImplemented
        return self.filename == other.filename

    def __hash__(self) -> int:
        return hash(id(self))

    def get_input_args(self) -> list[str]:
        """Returns command args for this input"""
        options = self.options.copy()
        args = []

        if format := options.pop("format", None):
            args.extend(["-f", str(format)])
        if video_size := options.pop("video_size", None):
            if isinstance(video_size, (tuple, list)) and len(video_size) == 2:
                video_size = f"{video_size[0]}x{video_size[1]}"
            args.extend(["-video_size", str(video_size)])

        args.extend(convert_kwargs_to_cmd_line_args(options))
        args.extend(["-i", self.filename])

        return args


class OutputNode(RunnableNode):
    """Nodes representing output files."""

    def __init__(
        self,
        filename: str,
        inputs: list["Stream"],
        output_options: dict[str, str | list[str]] = {},
    ):
        super().__init__()
        self.inputs: list[Stream] = inputs
        self.filename: str = filename
        self.output_options: dict[str, str | list[str]] = output_options

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OutputNode):
            return NotImplemented
        return self.filename == other.filename and self.inputs == other.inputs

    def __hash__(self) -> int:
        return hash(id(self))

    def _normalize_output_options(self):
        """Replaces keys names in output_options from human readable (passed by the user)"""
        """to names existing in ffmpeg docs, prepares for later use to build command"""
        """Casts option values to string"""
        keys_names_mapping = {
            "video_bitrate": "b:v",
            "audio_bitrate": "b:a",
            "format": "f",
        }
        self.output_options = {
            keys_names_mapping.get(k, k): v for k, v in self.output_options.items()
        }

        video_size = self.output_options.get("video_size")
        if isinstance(video_size, Sequence) and not isinstance(video_size, str):
            try:
                width, height = video_size
            except ValueError:
                raise ValueError(
                    "video_size must contain exactly two elements: (width, height)"
                )
            self.output_options["video_size"] = f"{width}x{height}"

    def get_output_args(self, enforce_output_mapping) -> list[str]:
        """Builds command args representing the output"""
        """Generates args for output options"""
        """Generates args for mapping streams to the output if neccessary"""
        args: list[str] = []
        self._normalize_output_options()
        options = self.output_options.copy()
        format = options.pop("f", None)
        args.extend(convert_kwargs_to_cmd_line_args(options, sort=False))

        if (
            len(self.inputs) == 1
            and isinstance(self.inputs[0].source_node, InputNode)
            and not isinstance(self.inputs[0], (TypedStream, IndexedStream))
            and not enforce_output_mapping
        ):
            args.append(self.filename)
            return args

        for input in self.inputs:
            args.append("-map")
            args.append(
                f"[{input.index}]"
                if isinstance(input.source_node, FilterNode)
                else input.index
            )

        if format:
            args.extend(["-f", str(format)])

        args.append(self.filename)

        return args


class MergedOutputNode(RunnableNode):
    """Node representing multiple outputs"""

    def __init__(self, outputs: Sequence[OutputNode]):
        super().__init__()
        self.outputs: tuple[OutputNode] = tuple(outputs)


class SinkNode(RunnableNode):
    """
    Represents a graph terminal node that is a sink filter (e.g., nullsink, buffersink),
    not a file output.
    """

    def __init__(self, filter_node: "FilterNode"):
        super().__init__()
        self.filter_node = filter_node
        self.inputs = filter_node.inputs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SinkNode):
            return NotImplemented
        return self.filter_node == other.filter_node

    def __hash__(self) -> int:
        return hash(self.filter_node)


class FilterNode(ProcessableNode):
    """Nodes representing filter operations."""

    def __init__(
        self,
        filter_name: str,
        positional_arguments: tuple[str],
        named_arguments: dict[str, Any],
        inputs: list["Stream"],
        num_output_streams: int = 1,
    ):
        super().__init__(num_output_streams)
        self.filter_name: str = filter_name
        self.positional_arguments: tuple = positional_arguments
        self.named_arguments: dict = named_arguments
        self.inputs: list[Stream] = inputs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FilterNode):
            return NotImplemented
        return (
            self.filter_name == other.filter_name
            and self.positional_arguments == other.positional_arguments
            and self.named_arguments == other.named_arguments
            and self.inputs == other.inputs
        )

    def __hash__(self) -> int:
        return hash(id(self))

    def get_command_string(self) -> str:
        """Builds a command string based on this filter"""
        input_streams = [f"[{input.index}]" for input in self.inputs]
        output_streams = [f"[{output.index}]" for output in self.output_streams]

        postional_arguments = (str(arg) for arg in self.positional_arguments)

        named_arguments = []
        for name, value in sorted(self.named_arguments.items()):
            if value is None:
                continue

            if value is True:
                value = "true"
            elif value is False:
                value = "false"

            val_escaped = escape_filter_description(escape_filter_option(value))
            named_arguments.append(f"{name}={val_escaped}")

        all_arguments = [*postional_arguments, *named_arguments]
        arguments_string = ":".join(all_arguments)

        return f"{''.join(input_streams)}{self.filter_name}{f'=' if arguments_string else ''}{arguments_string}{''.join(output_streams)}"


class Stream(GeneratedFiltersMixin):
    """Represents a single output stream from a node."""

    def __init__(self, source_node: Node):
        self.source_node: Node = source_node
        self.index: str | None = None
        self.elementary_streams: dict[str, TypedStream | IndexedStream] = {}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stream):
            return NotImplemented
        return self.source_node == other.source_node

    def __hash__(self) -> int:
        return hash(id(self))

    @property
    def audio(self) -> "TypedStream":
        return self.elementary_streams.setdefault("a", TypedStream("audio", self))

    @property
    def video(self) -> "TypedStream":
        return self.elementary_streams.setdefault("v", TypedStream("video", self))

    def __getitem__(self, key: str) -> "TypedStream | IndexedStream":
        """Allows accessing elementary stream contained in this Stream"""
        mapping = {"a": "audio", "v": "video"}
        if not isinstance(key, str) or len(key) != 1:
            raise TypeError("Expected string index (e.g. 'a')")

        if key in mapping:
            stream_type = mapping[key]
            return self.elementary_streams.setdefault(
                key, TypedStream(stream_type, self)
            )

        if key.isdigit():
            return self.elementary_streams.setdefault(key, IndexedStream(self))

        raise KeyError(
            f"Invalid stream key: {key!r}. Expected 'a', 'v', or a numeric index like '1'."
        )

    @property
    def node(self):
        """Returns the list of output streams produced by the filter node
        that generated this stream."""
        if not isinstance(self.source_node, FilterNode):
            raise AttributeError(".node is only available on filter outputs")
        return self.source_node.output_streams

    def _apply_filter(
        self,
        filter_name: str,
        postional_arguments: tuple = (),
        named_arguments: dict[str, Any] = {},
        inputs: list["Stream"] | None = None,
        num_output_streams: int = 1,
    ) -> list["Stream"]:
        """Creates a FilterNode and returns its output streams."""
        node = FilterNode(
            filter_name,
            postional_arguments,
            named_arguments,
            inputs or [self],
            num_output_streams,
        )
        return node.output_streams

    def _apply_dynamic_outputs_filter(
        self,
        filter_name: str,
        postional_arguments: tuple = (),
        named_arguments: dict[str, Any] = {},
        inputs: list["Stream"] | None = None,
    ) -> "FilterMultiOutput":
        """Creates a FilterNode and returns FilterMultiOutput to allow dynamic outputs."""
        filter_node = FilterNode(
            filter_name,
            postional_arguments,
            named_arguments,
            inputs or [self],
            num_output_streams=0,
        )
        return FilterMultiOutput(filter_node)

    def _apply_sink_filter(
        self,
        filter_name: str,
        named_arguments: dict = {},
        inputs: list["Stream"] | None = None,
    ) -> SinkNode:
        filter_node = FilterNode(
            filter_name,
            positional_arguments=(),
            named_arguments=named_arguments,
            inputs=inputs or [self],
            num_output_streams=0,
        )
        return SinkNode(filter_node)

    def filter(self, filter_name: str, *args, **kwargs) -> "Stream":
        """Custom filter with a single input and a single output"""
        return self._apply_filter(filter_name, args, kwargs)[0]

    def filter_multi_output(
        self, filter_name: str, *args, **kwargs
    ) -> "FilterMultiOutput":
        """Creates a custom filter allowing dynamic creation of output streams"""
        node = FilterNode(
            filter_name=filter_name,
            positional_arguments=args,
            named_arguments=kwargs,
            inputs=[self],
            num_output_streams=0,
        )
        return FilterMultiOutput(node)

    def output(
        self,
        filename: str,
        streams: list["Stream"] | None = None,
        format: str | None = None,
        vcodec: str | None = None,
        acodec: str | None = None,
        video_bitrate: str | int | None = None,
        audio_bitrate: str | int | None = None,
        aspect: str | float | None = None,
        frames: int | None = None,
        shortest: bool = False,
        **kwargs,
    ) -> "OutputNode":
        """
        Creates an output node for this stream, optionally muxing other streams.

        Args:
            filename (str): The output file path or URL.
            streams (list[Stream] | None): Additional streams to include in the output
                (e.g., audio tracks, subtitles) alongside the current stream.
            format (str | None): Force output format (ffmpeg flag: ``-f``).
            vcodec (str | None): Video codec (ffmpeg flag: ``-c:v``).
            acodec (str | None): Audio codec (ffmpeg flag: ``-c:a``).
            video_bitrate (str | int | None): Video bitrate (ffmpeg flag: ``-b:v``).
            audio_bitrate (str | int | None): Audio bitrate (ffmpeg flag: ``-b:a``).
            aspect (str | float | None): Set aspect ratio (ffmpeg flag: ``-aspect``).
            frames (int | None): Number of video frames to output (ffmpeg flag: ``-frames:v``).
            shortest (bool): Finish encoding when the shortest input stream ends.
            **kwargs: Additional output options.

        Returns:
            OutputNode: The created output node.
        """

        output_streams = [self]

        if streams is not None:
            output_streams.extend(streams)

        options = kwargs.copy()

        if format is not None:
            options["f"] = format
        if vcodec is not None:
            options["c:v"] = vcodec
        if acodec is not None:
            options["c:a"] = acodec
        if video_bitrate is not None:
            options["b:v"] = video_bitrate
        if audio_bitrate is not None:
            options["b:a"] = audio_bitrate
        if aspect is not None:
            options["aspect"] = aspect
        if frames is not None:
            options["frames:v"] = frames
        if shortest:
            options["shortest"] = None

        return OutputNode(filename, output_streams, output_options=options)


class TypedStream(Stream):
    """Elementary stream representing specific type of media out of those contained within a Stream"""

    def __init__(self, type: str, source_stream: Stream):
        self.type = type
        self.source_node = source_stream.source_node
        self.index: str | None = None

    def __getitem__(self, _):
        """Raises ValueError"""
        mapping = {"audio": "a", "video": "v"}
        raise ValueError(f"Stream already has a selector: {mapping[self.type]}")


class IndexedStream(Stream):
    """Elementary stream represented by index within the containing stream"""

    def __init__(self, source_stream: Stream):
        self.source_node = source_stream.source_node
        self.label: str
        self.index: str | None = None

    def __getitem__(self, _):
        """Raises ValueError"""
        raise ValueError(f"Stream already has a selector")


class GraphSorter:
    def __init__(self, output: RunnableNode):
        self.start_node: RunnableNode = output
        self.visited: set[Node] = set()
        self.sorted: list[Node] = []
        self.current_input_stream_index = 0
        self.current_filter_stream_index = 0

    def sort(self) -> list[Node]:
        self._sort(self.start_node)
        type_order = {InputNode: 0, FilterNode: 1, SinkNode: 2, OutputNode: 3}
        self.sorted.sort(key=lambda x: type_order[type(x)])
        self.label_streams()
        return self.sorted

    def _sort(self, node: Node) -> None:
        if node in self.visited:
            return
        self.visited.add(node)

        if isinstance(node, (FilterNode, SinkNode, OutputNode)):
            for stream in node.inputs:
                self._sort(stream.source_node)

        if isinstance(node, MergedOutputNode):
            for output in node.outputs:
                self._sort(output)
            return

        self.sorted.append(node)

    def label_streams(self) -> None:
        for node in self.sorted:
            if isinstance(node, InputNode):
                for stream in node.output_streams:
                    stream.index = str(self.current_input_stream_index)
                    self.label_elementary_streams(stream)
                    self.current_input_stream_index += 1
            if isinstance(node, FilterNode):
                for stream in node.output_streams:
                    stream.index = f"s{self.current_filter_stream_index}"
                    self.label_elementary_streams(stream)
                    self.current_filter_stream_index += 1

    def label_elementary_streams(self, stream: Stream):
        for type, elementary_stream in stream.elementary_streams.items():
            elementary_stream.index = f"{stream.index}:{type}"


class CommandBuilder:
    def __init__(self, nodes: list[Node], global_options: list = []):
        self.nodes: list[Node] = nodes
        self.global_options: list[str] = global_options

    def build_args(self) -> list[str]:
        args: list[str] = []
        filters = []
        outputs = []
        filter_complex: bool = False
        multi_input: bool = True if isinstance(self.nodes[1], InputNode) else False
        enforce_output_mapping: bool = False
        for node in self.nodes:
            if isinstance(node, InputNode):
                args.extend(node.get_input_args())
            if isinstance(node, FilterNode):
                if not filter_complex:
                    args.append("-filter_complex")
                    filter_complex = True

                filters.append(node.get_command_string())

            if isinstance(node, SinkNode):
                if not filter_complex:
                    args.append("-filter_complex")
                    filter_complex = True
                filters.append(node.filter_node.get_command_string())

            if isinstance(node, OutputNode):
                outputs.extend(node.get_output_args(enforce_output_mapping))
                if multi_input:
                    enforce_output_mapping = True

        if filters:
            args.append(";".join(filters))
        args.extend(outputs)

        args.extend(self.global_options)

        return args


class FilterMultiOutput:
    """Filter node wrapper which allows creating arbitrary outputs for the filter node dynamically"""

    def __init__(self, filter_node: FilterNode):
        self.filter_node = filter_node
        self.stream_cache: dict[str, Stream] = {}

    def __getitem__(self, key: str | int) -> "Stream":
        """Returns new or existing stream under label"""
        label = str(key)
        if label in self.stream_cache:
            return self.stream_cache[label]

        new_stream = Stream(self.filter_node)
        self.filter_node.output_streams.append(new_stream)
        self.stream_cache[label] = new_stream
        return new_stream
