import unittest

from local_env import SOURCE
from poetex.file_manager.manager import get_list_of_files
from poetex.poetry import load_poem


class TestLoadPoem(unittest.TestCase):
    def test_T01_load_poem(self):
        poems = get_list_of_files(SOURCE)
        poem = load_poem(poems[0])

        self.assertEqual(len(poem.stanzas), 6)


if __name__ == "__main__":
    unittest.main()
