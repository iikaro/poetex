import re
import sys

TYPES = r"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test|Merge ){1}"
COMMIT_PATTERN = TYPES + r"(\([\w\-\.]+\))?(!)?: ([\w ])+([\s\S]*)"


def _get_stripped_file_contents(file_path: str) -> str:
    """
    Return message to be committed.

    :param file_path: Absolute file path.
    :return: Stripped file contents.
    """

    with open(file_path) as file:
        commit_message = file.read()

    return commit_message.strip()


def check_commit_message(file_path: str) -> None:
    """
    Read current commit message and raise exception if it does not follow conventional commit format.

    :param file_path: Absolute file path to file with current commit message.
    :return: Raises a SystemExit exception if message does not follow correct format.
    """
    commit_message = _get_stripped_file_contents(file_path)

    if not re.match(COMMIT_PATTERN, commit_message):
        print("Error: Commit message does not match conventional commit styling.")
        sys.exit(1)


if __name__ == "__main__":
    check_commit_message(sys.argv[1])
