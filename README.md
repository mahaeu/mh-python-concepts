# mh-python-concepts



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
