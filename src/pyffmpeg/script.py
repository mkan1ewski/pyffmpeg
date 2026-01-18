import subprocess
from pathlib import Path

from pyffmpeg.parser import Parser
from pyffmpeg.generator import CodeGenerator

FILTERS_OUTPUT = Path("src/pyffmpeg/generated_filters.py")
SOURCES_OUTPUT = Path("src/pyffmpeg/sources.py")


def get_filters_to_process() -> list[dict]:
    """
    Gets all filter names for processing from ffmpeg -filters.
    Identifies sources (|->) and standard filters (->).
    Includes sinks (->|).
    """
    try:
        result = subprocess.run(["ffmpeg", "-filters"], capture_output=True, text=True)
    except FileNotFoundError:
        print("❌ Did not find ffmpeg")
        return []

    filters_metadata = []
    seen = set()

    for line in result.stdout.splitlines():
        parts = line.split()

        if len(parts) < 3:
            continue
        name = parts[1]
        io_specifier = parts[2]

        if "->" not in io_specifier:
            continue

        if name in seen:
            continue
        seen.add(name)

        item = {"name": name}

        if io_specifier.startswith("|"):
            item["is_source"] = True
        else:
            item["is_source"] = False

        filters_metadata.append(item)

    filters_metadata.sort(key=lambda x: x["name"])
    return filters_metadata


def get_ffmpeg_help(filter_name: str) -> str:
    """Gets raw text from ffmpeg help."""
    try:
        result = subprocess.run(
            ["ffmpeg", "--help", f"filter={filter_name}"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        print(f"⚠️  Couldn't get help for: {filter_name}")
        return ""


def generate_files():
    """Generates filters to generated_filters.py and sources to sources.py"""
    print(f"Starting generation...")
    print(f" - Filters -> {FILTERS_OUTPUT}")
    print(f" - Sources -> {SOURCES_OUTPUT}")

    with (
        open(FILTERS_OUTPUT, "w", encoding="utf-8") as f_filters,
        open(SOURCES_OUTPUT, "w", encoding="utf-8") as f_sources,
    ):
        f_filters.write("# --- AUTO-GENERATED FILE ---\n")
        f_filters.write("from typing import TYPE_CHECKING, Literal\n\n")
        f_filters.write("if TYPE_CHECKING:\n")
        f_filters.write(
            "    from pyffmpeg.node import Stream, FilterMultiOutput, SinkNode\n\n"
        )

        f_filters.write("class GeneratedFiltersMixin:\n")
        f_filters.write('    """\n')
        f_filters.write("    Mixin class containing auto-generated filter methods.\n")
        f_filters.write("    This class should be inherited by the Stream class.\n")
        f_filters.write('    """\n')

        f_sources.write("# --- AUTO-GENERATED FILE ---\n")
        f_sources.write("from typing import TYPE_CHECKING, Literal\n")
        f_sources.write("from pyffmpeg._utils import create_source\n\n")
        f_sources.write("if TYPE_CHECKING:\n")
        f_sources.write("    from pyffmpeg.node import Stream, FilterMultiOutput\n\n")

        items = get_filters_to_process()
        total_count = len(items)
        print(f"     Found {total_count} items to process.")

        success_count = 0
        for item in items:
            name = item["name"]
            is_source = item["is_source"]

            print(f"    Parsing: {name}...", end=" ")

            help_text = get_ffmpeg_help(name)
            if not help_text:
                print("❌ No help")
                continue

            try:
                parser = Parser(help_text)
                data = parser.parse()

                generator = CodeGenerator(data, is_source=is_source)
                code = generator.generate()

                if is_source:
                    f_sources.write(code + "\n\n")
                else:
                    f_filters.write(code + "\n\n")

                print("✅")
                success_count += 1

            except Exception as e:
                print(f"❌ Error: {e}")

    print(f"\n Finished. Generated {success_count}/{total_count} items.")


if __name__ == "__main__":
    generate_files()
