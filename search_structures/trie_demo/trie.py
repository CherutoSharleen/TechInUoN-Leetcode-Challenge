from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word.lower():
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def has_word(self, word: str) -> bool:
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def completions(self, prefix: str, limit: int = 10) -> list[str]:
        node = self.root
        prefix = prefix.lower()
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results: list[str] = []
        self._dfs(node, prefix, results, limit)
        return results

    def _dfs(self, node: TrieNode, current: str, results: list[str], limit: int) -> None:
        if len(results) >= limit:
            return
        if node.is_end:
            results.append(current)
        for char in sorted(node.children.keys()):
            self._dfs(node.children[char], current + char, results, limit)
