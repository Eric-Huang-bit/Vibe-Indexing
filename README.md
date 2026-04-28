# Vibe-Indexing

**Vibe-Indexing** is a Python toolkit for generating and indexing audio descriptions (AD) for video content, with support for film-grammar-aware analysis and multimodal LLM backends.

---

## Purpose

Vibe-Indexing provides a clean, extensible pipeline to:

- Extract frames from video clips
- Generate natural-language audio descriptions via multimodal APIs (e.g., Qwen VL, GPT-4o)
- Index and retrieve generated descriptions

---

## Quickstart

### Requirements

- Python 3.11+
- [pip](https://pip.pypa.io/)

### Install

```bash
git clone https://github.com/Eric-Huang-bit/Vibe-Indexing.git
cd Vibe-Indexing
pip install -e ".[dev]"
```

### Run the CLI

```bash
python -m vibe_indexing --help
```

---

## Development

### Setup

```bash
pip install -e ".[dev]"
```

### Lint

```bash
ruff check .
black --check .
```

### Tests

```bash
pytest
```

### Format

```bash
black .
ruff check --fix .
```

---

## Project Structure

```
Vibe-Indexing/
├── src/
│   └── vibe_indexing/      # Main package
│       ├── __init__.py
│       └── __main__.py     # CLI entrypoint
├── tests/                  # Test suite
├── scripts/                # Utility scripts
├── docs/                   # Documentation
├── pyproject.toml
└── README.md
```

---

## License

[MIT](LICENSE)
