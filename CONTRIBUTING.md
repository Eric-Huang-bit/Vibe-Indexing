# Contributing to Audio-Description

Thank you for your interest in contributing! Below are guidelines to help you get started.

## Getting Started

1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/Audio-Description.git
   cd Audio-Description
   ```

2. Install the development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Create a new branch for your change:
   ```bash
   git checkout -b my-feature
   ```

## Making Changes

- Keep changes focused and minimal.
- Follow the existing code style (enforced by `ruff` and `black`).
- Add or update tests for any new or changed behaviour.

## Running Checks

```bash
# Lint
ruff check .
black --check .

# Tests
pytest
```

## Submitting a Pull Request

1. Push your branch to your fork.
2. Open a Pull Request against `main`.
3. Describe what you changed and why.
4. Ensure CI passes before requesting review.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).
