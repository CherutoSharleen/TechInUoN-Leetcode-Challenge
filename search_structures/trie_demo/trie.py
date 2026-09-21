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

    def prefix_count(self, prefix: str) -> int:
        return len(self.completions(prefix, limit=10_000))

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def first_completion(self, prefix: str) -> str | None:
        options = self.completions(prefix, limit=1)
        if not options:
            return None
        return options[0]

    def delete(self, word: str) -> bool:
        word = word.lower()

        def _delete(node: TrieNode, idx: int) -> tuple[bool, bool]:
            if idx == len(word):
                if not node.is_end:
                    return False, False
                node.is_end = False
                return True, len(node.children) == 0
            char = word[idx]
            child = node.children.get(char)
            if child is None:
                return False, False
            deleted, prune_child = _delete(child, idx + 1)
            if prune_child:
                del node.children[char]
            should_prune = (not node.is_end) and len(node.children) == 0
            return deleted, should_prune

        deleted, _ = _delete(self.root, 0)
        return deleted

    def _dfs(self, node: TrieNode, current: str, results: list[str], limit: int) -> None:
        if len(results) >= limit:
            return
        if node.is_end:
            results.append(current)
        for char in sorted(node.children.keys()):
            self._dfs(node.children[char], current + char, results, limit)
