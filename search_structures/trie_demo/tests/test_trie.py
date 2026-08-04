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

    def test_delete_word(self) -> None:
        trie = Trie()
        trie.insert("graph")
        self.assertTrue(trie.delete("graph"))
        self.assertFalse(trie.has_word("graph"))

    def test_prefix_count(self) -> None:
        trie = Trie()
        for word in ["graph", "greedy", "grid", "tree"]:
            trie.insert(word)
        self.assertEqual(trie.prefix_count("gr"), 3)

    def test_starts_with(self) -> None:
        trie = Trie()
        trie.insert("graph")
        self.assertTrue(trie.starts_with("gr"))
        self.assertFalse(trie.starts_with("xy"))


if __name__ == "__main__":
    unittest.main()
