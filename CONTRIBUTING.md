# Contributing to Mess Food Feedback Analyzer

Thank you for your interest in contributing! This document covers everything you need to get started — whether you're fixing a bug, adding a feature, or improving documentation.

> **GSSoC 2026 Contributors:** Please read the [GSSoC-specific rules](#gssoc-2026-rules) before opening any issue or PR.

---

## Table of Contents

- [Local Setup](#local-setup)
- [Project Structure](#project-structure)
- [Branch Naming Convention](#branch-naming-convention)
- [Commit Message Format](#commit-message-format)
- [Pull Request Checklist](#pull-request-checklist)
- [Code Style Guide](#code-style-guide)
- [Running Tests](#running-tests)
- [GSSoC 2026 Rules](#gssoc-2026-rules)

---

## Local Setup

### Prerequisites

- Python 3.9+
- Git

### Steps

1. **Fork** the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/mess-food-feedback-analyzer.git
   cd mess-food-feedback-analyzer
   ```

2. **Create a virtual environment** and activate it:
   ```bash
   python -m venv venv

   # On Linux/macOS:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** by copying the example file:
   ```bash
   cp .env.example .env
   # Fill in the required values in .env
   ```

5. **Run the app locally** to verify setup:
   ```bash
   python app.py
   ```

---

## Project Structure

```
mess-food-feedback-analyzer/
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── README.md
├── CONTRIBUTING.md         # This file
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       ├── feature_request.md
│       ├── documentation.md
│       └── config.yml
└── tests/                  # Test files
```

---

## Branch Naming Convention

Use the following prefixes for all branches:

| Prefix       | When to use                                      |
|--------------|--------------------------------------------------|
| `feat/`      | New feature or enhancement                       |
| `fix/`       | Bug fix                                          |
| `docs/`      | Documentation changes only                      |
| `test/`      | Adding or updating tests                         |
| `chore/`     | Build process, CI, dependency updates            |
| `refactor/`  | Code restructure without changing behaviour      |

**Examples:**
```
feat/add-rating-export
fix/sentiment-analysis-crash
docs/update-setup-instructions
```

Always branch off from `main`:
```bash
git checkout main
git pull origin main
git checkout -b feat/your-feature-name
```

---

## Commit Message Format

This project follows [Conventional Commits](https://www.conventionalcommits.org/).

**Format:**
```
<type>(<optional scope>): <short description>

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `style`, `perf`

**Examples:**
```
feat(analysis): add weekly summary chart
fix(api): handle empty feedback submission
docs: update environment variable instructions
test(sentiment): add unit tests for edge cases
```

- Use the **imperative mood** in the description ("add" not "added")
- Keep the first line under **72 characters**
- Reference the issue number in the footer: `Closes #100`

---

## Pull Request Checklist

Before submitting a PR, make sure you have:

- [ ] Branched off `main` with the correct naming prefix
- [ ] Written descriptive commit messages (Conventional Commits)
- [ ] Added or updated tests for your changes
- [ ] Run `flake8` and resolved all linting issues
- [ ] Verified the app runs locally without errors
- [ ] Filled in the PR template completely
- [ ] Linked the issue your PR resolves (`Closes #<issue-number>`)
- [ ] Not included unrelated changes in the same PR

---

## Code Style Guide

This project follows **PEP 8** and is linted with **flake8**.

### Install flake8

```bash
pip install flake8
```

### Run the linter

```bash
flake8 .
```

### Key rules

- **4 spaces** for indentation (no tabs)
- **Max line length: 79 characters**
- Blank line between top-level functions and classes
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Remove unused imports and variables before committing

---

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run a specific test file
python -m pytest tests/test_sentiment.py
```

All PRs must pass existing tests. If you're adding a new feature, add corresponding tests in the `tests/` directory.

---

## GSSoC 2026 Rules

To keep the project healthy and fair during GSSoC:

1. **One contributor per issue.** Comment on the issue to express interest and wait for a maintainer to assign it to you before starting work. Do not submit a PR for an unassigned issue.

2. **No spam PRs.** PRs that only add whitespace, rename variables arbitrarily, or make cosmetic changes with no functional value will be closed without merging.

3. **No duplicate PRs.** Check existing open PRs before submitting. If a PR already addresses the issue, contribute a review comment instead.

4. **Respect review feedback.** Address all review comments before requesting a re-review. Do not close and reopen PRs to avoid feedback.

5. **One issue at a time.** Complete and close your current assigned issue before requesting assignment on another.

Violations may result in disqualification from GSSoC contribution tracking on this project.

---

## Need Help?

- Open a [GitHub Discussion](../../discussions) for questions — please don't open issues for general questions.
- For urgent blockers, leave a comment on the relevant issue.
