from local_env import SOURCE
from poetex.latex.builder import compile_latex


def populate_build_directory(source: str = SOURCE) -> None:
    compile_latex(source, False)


if __name__ == "__main__":
    populate_build_directory()
