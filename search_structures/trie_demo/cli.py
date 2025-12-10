from __future__ import annotations

from trie import Trie


WORDS = [
    "array",
    "arithmetic",
    "binary",
    "bitwise",
    "graph",
    "greedy",
    "heap",
    "hashmap",
    "linkedlist",
    "queue",
    "stack",
    "tree",
]


def main() -> None:
    trie = Trie()
    for word in WORDS:
        trie.insert(word)

    print("Trie Prefix Search Demo")
    prefix = input("Enter prefix: ").strip().lower()
    matches = trie.completions(prefix)
    if not matches:
        print("No completions found.")
        return
    print("Completions:")
    for word in matches:
        print(f"- {word}")


if __name__ == "__main__":
    main()
