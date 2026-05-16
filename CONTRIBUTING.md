# Contributing to Mess Food Feedback Analyzer

Thanks for your interest in contributing! This project is part of **GSSoC 2026** and welcomes contributions of all kinds — bug fixes, new features, documentation, and tests.

Please read this guide before opening a PR so your contribution gets merged smoothly.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [How to Contribute](#how-to-contribute)
- [Branch Naming](#branch-naming)
- [Commit Messages](#commit-messages)
- [Pull Request Checklist](#pull-request-checklist)
- [Code Style](#code-style)
- [Running Tests](#running-tests)
- [Reporting Bugs](#reporting-bugs)
- [GSSoC Guidelines](#gssoc-guidelines)

---

## Code of Conduct

Be respectful, inclusive, and constructive. Harassment of any kind will not be tolerated.

---

## Getting Started

### 1. Fork and clone

```bash
git clone https://github.com/<your-username>/mess-food-feedback-analyzer.git
cd mess-food-feedback-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
# Train the model
python model/train_model.py

# Run analysis
python analysis.py

# Launch Streamlit UI
streamlit run app.py
```

### 5. Run tests

```bash
pytest tests/ -v
```

---

## Project Structure

```
mess-food-feedback-analyzer/
├── data/
│   └── mess_data.csv          # Feedback dataset
├── model/
│   └── train_model.py         # Model training script
├── utils/
│   └── validator.py           # Input validation module
├── tests/
│   └── test_validator.py      # Unit tests
├── outputs/                   # Generated charts (git-ignored)
├── analysis.py                # Data visualisation script
├── app.py                     # Streamlit web UI
├── requirements.txt           # Python dependencies
└── README.md
```

---

## How to Contribute

1. **Check existing issues** — look at the [Issues tab](../../issues) before starting work. Comment on the issue to get it assigned to you.
2. **Don't work on unassigned issues** — especially during GSSoC, only work on issues assigned to you.
3. **One PR per issue** — keep changes focused. Don't bundle multiple unrelated fixes.
4. **Open an issue first** for any non-trivial change — discuss the approach before writing code.

---

## Branch Naming

Use the format: `<type>/<short-description>`

| Type | When to use | Example |
|------|-------------|---------|
| `feat` | New feature | `feat/streamlit-ui` |
| `fix` | Bug fix | `fix/analysis-mean-bug` |
| `docs` | Documentation only | `docs/update-readme` |
| `test` | Adding or fixing tests | `test/validator-edge-cases` |
| `chore` | Config, tooling, CI | `chore/add-gitignore` |
| `refactor` | Code cleanup, no behaviour change | `refactor/train-model-cleanup` |

---

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

[optional body]

[optional footer — e.g. Closes #12]
```

**Examples:**

```
feat(validator): add FeedbackInput dataclass with range checks

fix(analysis): exclude overall_rating from feature bar chart

docs(readme): add setup guide and screenshots

test(validator): add 32 unit tests for all edge cases

Closes #9
```

Rules:
- Use the **imperative mood** — "add feature" not "added feature"
- Keep the summary under **72 characters**
- Reference the issue number in the footer when applicable

---

## Pull Request Checklist

Before submitting your PR, make sure:

- [ ] Code runs without errors locally
- [ ] All existing tests pass (`pytest tests/ -v`)
- [ ] New tests added for any new functionality
- [ ] No commented-out code or debug `print()` statements left in
- [ ] PR title follows Conventional Commits format
- [ ] PR description references the issue (`Closes #<number>`)
- [ ] You have not modified files unrelated to your issue

---

## Code Style

This project follows [PEP 8](https://pep8.org/). Key rules:

- **Indentation:** 4 spaces (no tabs)
- **Line length:** max 100 characters
- **Imports:** grouped — stdlib → third-party → local, separated by blank lines
- **Naming:** `snake_case` for variables and functions, `PascalCase` for classes
- **Docstrings:** use triple-quoted strings for all public functions and classes

You can check your code with:

```bash
pip install flake8
flake8 . --max-line-length=100 --exclude=venv,__pycache__
```

---

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_validator.py -v

# Run with coverage report
pip install pytest-cov
pytest tests/ --cov=utils --cov-report=term-missing
```

All PRs must pass existing tests. New features must include tests.

---

## Reporting Bugs

Use the **Bug Report** issue template. Include:

- What you expected to happen
- What actually happened (paste the full error traceback)
- Steps to reproduce
- Your Python version (`python --version`)
- Your OS

---

## GSSoC Guidelines

- Only **one contributor per issue** — do not duplicate work.
- Spam PRs (tiny edits, whitespace changes, README typo fixes unrelated to any issue) will be closed without review.
- Be patient — maintainers are volunteers. Allow 2–3 days for review.
- If your PR has been open for more than 5 days with no response, feel free to leave a polite comment.
- All contributors must follow the GSSoC Code of Conduct in addition to this project's guidelines.

---

Happy contributing! If you have any questions, open a [Discussion](../../discussions) or comment on the relevant issue.