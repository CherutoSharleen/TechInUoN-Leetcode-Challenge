import unittest

from trie import Trie


class TrieTests(unittest.TestCase):
    def test_insert_and_lookup(self) -> None:
        trie = Trie()
        trie.insert("graph")
        self.assertTrue(trie.has_word("graph"))
        self.assertFalse(trie.has_word("gra"))

    def test_prefix_completions(self) -> None:
        trie = Trie()
        for word in ["graph", "greedy", "grid", "tree"]:
            trie.insert(word)
        self.assertEqual(trie.completions("gr"), ["graph", "greedy", "grid"])


if __name__ == "__main__":
    unittest.main()
