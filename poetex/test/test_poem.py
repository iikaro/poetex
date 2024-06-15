import unittest

from local_env import SOURCE
from poetex.latex.builder import compile_latex
from poetex.poetry.poetry import load_poem
from poetex.utils.utils import get_list_of_files


class TestLoadPoem(unittest.TestCase):
    def test_T01_load_poem(self):
        poems = get_list_of_files(SOURCE)
        poem = load_poem(poems[0])
        print(f"First Verse\n{poem.stanzas[0].verses[0]}\n")
        print(f"First Stanza\n{poem.stanzas[0]}\n")
        print(f"First Poem\n{poem}")
        self.assertEqual(len(poem.stanzas), 5)

    def test_T02_load_multiple_poems(self):
        paths = get_list_of_files(SOURCE)
        poems = [load_poem(path) for path in paths]
        self.assertEqual(len(poems), 1)

    @unittest.skip("Skip until Github Actions is configured to run LaTeX commands")
    def test_T03_compile_latex(self):
        compile_latex(SOURCE)

    def test_T04_verify_poem_object_is_json_serializable(self):
        paths = get_list_of_files(SOURCE)
        poems = [load_poem(path) for path in paths]
        schema = poems[0].model_json_schema()
        self.assertIsNotNone(schema)
