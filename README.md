# File Spliter Script


A Pretty simple script in python3, to split a text file in several chunks.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies and the virtual environment:

    uv sync

## Usage

The script can be executed as follows:

    uv run python3 splitter.py -i <file_path> -l <number_of_lines_per_chunk>
    
It is also possible to informe an output directory:

    uv run python3 splitter.py -i <file_path> -l <number_of_lines_per_chunk> -o <output directory>
