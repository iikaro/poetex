import os
import os.path
import shutil
import subprocess

from local_env import ROOT
from poetex.constants import TEX_EXTENSION
from poetex.poem import Poem
from poetex.poetry import load_poem
from poetex.utils import to_snake_case, get_list_of_files

OUTPUT_DIR = "build"
OUTPUT_PATH = os.path.join(ROOT, OUTPUT_DIR)
MAIN = "main.tex"
MAIN_AUX = "main.aux"
TITLE_PAGE = "title_page.tex"
REFERENCES = "references.bib"
TEMPLATES_DIR = "templates"
PATH = os.path.dirname(__file__)
POEMS_DIR = "poems"
MAIN_FILE_PATH = os.path.join(PATH, TEMPLATES_DIR, MAIN)
TITLE_PAGE_FILE_PATH = os.path.join(PATH, TEMPLATES_DIR, TITLE_PAGE)
REFERENCES_FILE_PATH = os.path.join(PATH, TEMPLATES_DIR, REFERENCES)
POEMS_KEY = "%#POEMS#"


def compile_latex(source: str, build: bool = True) -> None:
    """
    Make poetry LaTeX book from individual plain text files within source.

    :param source: Absolute path to where the individual poems are located.
    :param build: Whether to build the PDF or not. Defaults to False.
    """
    _create_output_directories()
    _copy_latex_templates_to_build_folder()

    poem_paths = get_list_of_files(source)
    poems = [load_poem(path) for path in poem_paths]
    poems_relative_path = _populate_template(poems)

    _add_poems_to_main_file(poems_relative_path)

    if build:
        _build()


def _add_poems_to_main_file(poems_relative_path: list[str]) -> None:
    """
    Include tex poems to the main tex file. The poems will be inserted where the key %#POEMS# is located by means of the
    \include{path} command.

    :param poems_relative_path: List with relative path of all tex poems.
    """
    # Read contents of main.tex
    with open(os.path.join(OUTPUT_PATH, MAIN), "r", encoding="utf-8") as file:
        main_file_contents = file.read()

    # Create list of \include{path} commands for each poem relative path
    poems_list_latex = [f'\\include{{{path.replace(os.sep, "/")}}}\n' for path in poems_relative_path]

    # Replace poems key by include command
    main_file_contents = main_file_contents.replace(POEMS_KEY, "".join(poems_list_latex))

    # Write back to main.tex file.
    with open(os.path.join(OUTPUT_PATH, MAIN), "w", encoding="utf-8") as file:
        file.write(main_file_contents)


def _populate_template(poems: list[Poem]) -> list[str]:
    """
    Convert plain text poem files (txt) into tex files and place them in the folder where PDF will be compiled.

    :param poems: List of poem objects.
    :return: List of relative path where to find the poems in tex format.
    """
    poems_relative_path = []
    for i, poem in enumerate(poems):
        language = f"\\selectlanguage{{{poem.language.value}}}"
        lines = f"\\poemlines{{{poem.lines}}}"
        title = f"\\poemtitle{{{poem.title}}}"
        poem_latex = poem.to_latex_verse()

        file_name = "_".join([str(i), to_snake_case(poem.title.text) + TEX_EXTENSION])

        latex_contents = "\n".join([language, lines, title, poem_latex])
        with open(os.path.join(OUTPUT_PATH, POEMS_DIR, file_name), "w", encoding="utf-8") as file:
            file.write(latex_contents)

        poems_relative_path.append(os.path.join(POEMS_DIR, file_name))

    return poems_relative_path


def _build():
    """Call LaTeX command to build PDF twice to generate table of contents."""
    main_tex_file_path = os.path.join(OUTPUT_PATH, MAIN)
    main_aux_file_path = os.path.join(OUTPUT_PATH, MAIN_AUX)
    command = ["pdflatex", "-output-directory=" + OUTPUT_PATH, main_tex_file_path]
    bibtex_command = [
        "bibtex",
        "--include-directory=" + OUTPUT_PATH,
        main_aux_file_path,
    ]
    try:
        subprocess.run(command, check=True)
        subprocess.run(bibtex_command, check=True)
        subprocess.run(command, check=True)
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {main_tex_file_path}: {e}")

    print("LaTeX compilation complete.")


def _copy_latex_templates_to_build_folder() -> None:
    """Copy template files (main.tex and title_path.tex) to the folder where the PDF will be compiled."""
    shutil.copy(MAIN_FILE_PATH, OUTPUT_PATH)
    shutil.copy(TITLE_PAGE_FILE_PATH, OUTPUT_PATH)
    shutil.copy(REFERENCES_FILE_PATH, OUTPUT_PATH)


def _create_output_directories() -> None:
    """Create build directory, and inner folders, where the PDF will be compiled, if it does not exist, at the root."""
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    if not os.path.exists(os.path.join(OUTPUT_PATH, POEMS_DIR)):
        os.makedirs(os.path.join(OUTPUT_PATH, POEMS_DIR))
