import os


def get_list_of_files(source: str) -> list[str]:
    """
    Return list of absolute file paths to files within source.
    :param source: Absolute file path to directory whose files will be listed.
    :return: List of absolute file paths.
    """
    files = [os.path.abspath(os.path.join(source, file)) for file in os.listdir(source) if
             file.endswith(".txt")]
    return files
