# Project Title
### Computational Thinking Foundations: Python, VS Code, and GitHub

# Required Dependencies
Before starting, make sure that you have installed the following dependencies:

- **[Python](https://www.python.org/downloads/) >= 3.14**
- **[pip](https://pip.pypa.io/en/stable/installation/) >= 26.2.1**

# How to set up the virtual environment

## Create a Python Virtual Environment
To create a Python virtual env (venv), run the following code:

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install pandas and matplotlib
Upgrade pip and install libraries.

```
# Update and upgrade pip version
pip install --upgrade pip
# Install pandas and matplotlib
pip install pandas matplotlib
```

Save the installed packages.

```
pip freeze > requirements.txt
```

# How to run Python scripts
To run the script, make sure to go inside the src folder first.

```
cd src
```

Then, run the python script using the following command:

```
python3 hello.py
```

# Answer to Reflections