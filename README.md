# mh-python-concepts

## How to use this repository

Learning Python means dealing with many concepts and an even larger number of details.
Focusing on too many details too early often slows learning down
and can make things unnecessarily confusing.

For that reason, each topic in this repository is split into two parts.

### Intro

The `intro/` sections focus on the core mechanics of a topic.

They are:
- self-contained
- minimal
- centered on how the concept is actually used

Each intro is designed to give you a solid first contact.
After working through it, you should be able to:
- understand the core idea
- use the concept in real code
- recognize it when you see it elsewhere

If your goal is to learn Python efficiently,
working through the intros alone is usually sufficient.

---

### Concepts

The `concepts/` sections go beyond the core mechanics.

They explore:
- internal details
- additional tools and variations
- distinctions that are not always needed in practice

These sections are not required to use the language effectively.

Instead, they exist to:
- deepen understanding
- make complex behavior less opaque
- build a more precise mental model

Having worked through the intro first
makes these sections much easier to understand.

---


## Setup your environment

This repository is intended to be used with Python and Jupyter notebooks.

### 1. Select a Python version

Python 3.11 or newer is recommended.

If you use `pyenv`:

```bash
pyenv install 3.11.9    # if not already installed
pyenv local 3.11.9
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Activate it:**

  ```bash
  source .venv/bin/activate # for MacOS / Linux
  ```

  ```powershell
  .venv\Scripts\Activate.ps1 # for Windows PowerShell
  ```

### 3. Install dependencies

To use the notebooks:

```bash
pip install .
```

For development

```bash
pip install -e ".[dev]"
```

You can now explore the notebooks and examples in this repository.



---

## License & Usage

This repository is provided as an external learning resource.

You are welcome to use and fork it for learning purposes.
Redistribution or inclusion in other teaching repositories
is not permitted.

Original repository:
https://github.com/mahaeu/mh-python-concepts

See LICENSE for full terms.
