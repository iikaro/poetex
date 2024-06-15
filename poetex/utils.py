import os
from typing import List


def to_snake_case(string: str) -> str:
    """Convert string to snake case."""
    return string.replace(" ", "_").lower()


def get_list_of_files(source: str) -> List[str]:
    """
    Return list of absolute file paths to files within source.

    :param source: Absolute file path to directory whose files will be listed.
    :return: List of absolute file paths.
    """
    files = [os.path.abspath(os.path.join(source, file)) for file in os.listdir(source) if file.endswith(".txt")]

    return files


def load_file_contents(file_path: str) -> str:
    """
    Load contents of text file into plain string.

    :param file_path: Path to file.
    :return: String with file contents.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents
