import subprocess
from pathlib import Path

from pyffmpeg.parser import Parser
from pyffmpeg.generator import CodeGenerator

OUTPUT_FILE = Path("src/pyffmpeg/generated_filters.py")


def get_filters_to_process() -> list[str]:
    """
    Gets all filter names for processing from ffmpeg -filters.
    Excludes sources and sinks.
    """
    try:
        result = subprocess.run(["ffmpeg", "-filters"], capture_output=True, text=True)
    except FileNotFoundError:
        print("❌ Did not found ffmpeg")
        return []

    filters = set()

    for line in result.stdout.splitlines():
        parts = line.split()

        if len(parts) < 3:
            continue
        name = parts[1]
        io_specifier = parts[2]

        if "->" not in io_specifier:
            continue

        # rejecting sources (|->...) and sinks (...->|)
        if not io_specifier.startswith("|") and not io_specifier.endswith("|"):
            filters.add(name)

    return sorted(list(filters))


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


def generate_file():
    """Generates all FIILTERS methods to OUTPUT_FILE"""
    print(f"Starting generation to {OUTPUT_FILE}...")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# --- AUTO-GENERATED FILE ---\n\n")
        f.write("from typing import TYPE_CHECKING, Literal\n")

        f.write("if TYPE_CHECKING:\n")
        f.write("    from pyffmpeg.node import Stream\n\n")

        f.write("class GeneratedFiltersMixin:\n")
        f.write('    """\n')
        f.write("    Mixin class containing auto-generated filter methods.\n")
        f.write("    This class should be inherited by the Stream class.\n")
        f.write('    """\n')

        filters = get_filters_to_process()
        filters_count = len(filters)
        print(f"     Found {filters_count} filters.")

        success_count = 0
        for filter_name in filters:
            print(f"    Parsing: {filter_name}...", end=" ")

            help_text = get_ffmpeg_help(filter_name)
            if not help_text:
                print("❌ Did not find help")
                continue

            try:
                parser = Parser(help_text)
                data = parser.parse()

                generator = CodeGenerator(data)
                code = generator.generate()

                f.write(code + "\n\n")
                print("✅")
                success_count += 1

            except Exception as e:
                print(f"❌ Error: {e}")

    print(f"\n Finished. Generated {success_count}/{filters_count} methods.")


if __name__ == "__main__":
    generate_file()
