# Trie Prefix Search Demo

This educational mini application implements a Trie data structure and uses it for prefix-based search over fictional DSA vocabulary.

## What it teaches

- Trie insertion and terminal markers
- Exact word lookup
- Prefix traversal and completion generation

## Installation

No third-party dependencies.

```bash
python --version
```

## Run

```bash
cd search_structures/trie_demo
python cli.py
```

## Test

```bash
cd search_structures/trie_demo
python -m unittest discover -s tests -p "test_*.py"
```

## Example

Input:

```text
gr
```

Output:

```text
Completions:
- graph
- greedy
- ...
```

## Components

- `trie.py`: Trie and completion logic
- `cli.py`: command-line interaction
- `tests/test_trie.py`: basic correctness tests

## Data note

Word list is fictional/synthetic.

## Limitations and exercises

- Current implementation is case-insensitive and ASCII-focused.
- Extend with frequency ranking and fuzzy prefix matching.

## Disclosure

This is a retrospective educational addition created now. Historical author dates may be used for commit metadata and do not indicate the actual execution date of this work.
