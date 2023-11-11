import unittest

from poetex.poetry import load_poem


class TestLoadPoem(unittest.TestCase):
    def test_T01_load_poem(self):
        poem = load_poem(r'..\..\source\morning_song.txt')
        self.assertEqual(len(poem.stanzas), 6)
