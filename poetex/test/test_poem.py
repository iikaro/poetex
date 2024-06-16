import pytest
from local_env import SOURCE
from poetex.latex.builder import compile_latex
from poetex.poetry.poetry import load_poem
from poetex.utils.utils import get_list_of_files


def test_load_poem():
    poems = get_list_of_files(SOURCE)
    poem = load_poem(poems[0])
    print(f"First Verse\n{poem.stanzas[0].verses[0]}\n")
    print(f"First Stanza\n{poem.stanzas[0]}\n")
    print(f"First Poem\n{poem}")
    assert len(poem.stanzas) == 5


def test_load_multiple_poems():
    paths = get_list_of_files(SOURCE)
    poems = [load_poem(path) for path in paths]
    assert len(poems) == 1


@pytest.mark.skip(reason="Skip until Github Actions is configured to run LaTeX commands")
def test_compile_latex():
    compile_latex(SOURCE)


def test_verify_poem_object_is_json_serializable():
    paths = get_list_of_files(SOURCE)
    poems = [load_poem(path) for path in paths]
    schema = poems[0].model_json_schema()
    assert schema is not None
