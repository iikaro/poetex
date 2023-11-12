# fonts: libertine, paladino, stinx, fouriernc
import os
import os.path
import shutil
import subprocess

from local_env import ROOT
from poetex.constants import TEX_EXTENSION
from poetex.poem import Poem

OUTPUT_DIR = "build"
OUTPUT_PATH = os.path.join(ROOT, OUTPUT_DIR)
MAIN = "main.tex"
TITLE_PAGE = "title_page.tex"
TEMPLATES_DIR = "templates"
PATH = os.path.dirname(__file__)
POEMS_DIR = "poems"
MAIN_FILE_PATH = os.path.join(PATH, TEMPLATES_DIR, MAIN)
TITLE_PAGE_FILE_PATH = os.path.join(PATH, TEMPLATES_DIR, TITLE_PAGE)
POEMS_KEY = "%#POEMS#"


def populate_template(poems: list[Poem]) -> None:
    create_output_directories()
    copy_latex_templates_to_build_folder()

    poems_relative_path = []
    for i, poem in enumerate(poems):
        language = f"\\selectlanguage{{{poem.language.value}}}"
        lines = f"\\poemlines{{{poem.lines}}}"
        title = f"\\poemtitle{{{poem.title}}}"
        poem_latex = poem.to_latex_verse()

        file_name = "_".join([str(i), to_snake_case(poem.title.text) + TEX_EXTENSION])

        latex_contents = "\n".join([language, lines, title, poem_latex])
        with open(
            os.path.join(OUTPUT_PATH, POEMS_DIR, file_name), "w", encoding="utf-8"
        ) as file:
            file.write(latex_contents)

        poems_relative_path.append(os.path.join(POEMS_DIR, file_name))

    with open(os.path.join(OUTPUT_PATH, MAIN), "r", encoding="utf-8") as file:
        main_file_contents = file.read()

    poems_list_latex = [
        f'\\include{{{path.replace(os.sep, "/")}}}\n' for path in poems_relative_path
    ]
    main_file_contents = main_file_contents.replace(
        POEMS_KEY, "".join(poems_list_latex)
    )

    with open(os.path.join(OUTPUT_PATH, MAIN), "w", encoding="utf-8") as file:
        file.write(main_file_contents)


def build():
    main_tex_file_path = os.path.join(OUTPUT_PATH, MAIN)
    command = ["pdflatex", "-output-directory=" + OUTPUT_PATH, main_tex_file_path]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {main_tex_file_path}: {e}")

    print("LaTeX compilation complete.")


def to_snake_case(string: str) -> str:
    return string.replace(" ", "_").lower()


def copy_latex_templates_to_build_folder() -> None:
    shutil.copy(MAIN_FILE_PATH, OUTPUT_PATH)
    shutil.copy(TITLE_PAGE_FILE_PATH, OUTPUT_PATH)


def create_output_directories() -> None:
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    if not os.path.exists(os.path.join(OUTPUT_PATH, POEMS_DIR)):
        os.makedirs(os.path.join(OUTPUT_PATH, POEMS_DIR))
