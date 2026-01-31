# Nodes

This module contains all node types that make up the FFmpeg processing graph.

## Base Node Classes

::: pyffmpeg.node.Node
    options:
      show_root_heading: true
      show_source: false
      members:
        - __init__

::: pyffmpeg.node.ProcessableNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__

::: pyffmpeg.node.RunnableNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__
        - global_args
        - overwrite_output
        - get_args
        - compile
        - run
        - run_async

## Input/Output Nodes

::: pyffmpeg.node.InputNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__
        - get_input_args

::: pyffmpeg.node.OutputNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__
        - get_output_args

::: pyffmpeg.node.MergedOutputNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__

::: pyffmpeg.node.SinkNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__

## Filter Nodes

::: pyffmpeg.node.FilterNode
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__
        - get_command_string

::: pyffmpeg.node.FilterMultiOutput
    options:
      show_root_heading: true
      show_source: true

