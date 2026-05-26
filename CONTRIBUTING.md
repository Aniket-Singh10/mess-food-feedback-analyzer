# Contributing to MessFood Feedback Analyzer 🍽️

Thank you for your interest in contributing! This project is part of **GSSoC 2026** and welcomes beginners.

---

## 🚀 Getting Started

### 1. Fork the repository
Click the **Fork** button at the top-right of the GitHub repo page.

### 2. Clone your fork
```bash
git clone https://github.com/<your-username>/mess-food-feedback-analyzer.git
cd mess-food-feedback-analyzer
```

### 3. Create a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🌿 Branching Strategy

Always create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

---

## ✅ Pull Request Checklist

Before submitting a PR, make sure:
- [ ] Code runs without errors (`streamlit run app.py`)
- [ ] New functions have docstrings
- [ ] No hardcoded file paths
- [ ] No sensitive data committed
- [ ] PR title is descriptive (see Issue Naming Convention below)

---

## 📝 Issue Naming Convention

| Type | Title Format | Example |
|------|-------------|---------|
| Bug | `[BUG] Short description` | `[BUG] CSV upload crashes on empty file` |
| Feature | `[FEATURE] Short description` | `[FEATURE] Add dark/light mode toggle` |
| Enhancement | `[ENHANCEMENT] Short description` | `[ENHANCEMENT] Improve heatmap readability` |
| Documentation | `[DOCS] Short description` | `[DOCS] Add installation GIF to README` |
| Question | `[QUESTION] Short description` | `[QUESTION] How does the model handle NaNs?` |

---

## 💡 Good First Issues for Beginners

- Add input validation for slider values
- Improve the PDF report layout
- Add a new chart (e.g., box plot per factor)
- Write unit tests for `validate_csv()`
- Add a dark/light mode toggle
- Translate README to another language

---

## 📬 Code of Conduct

Be kind, inclusive, and constructive. This is a beginner-friendly project — everyone was a beginner once.

---

*Built for GSSoC 2026 🚀*
