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
python3 inspect_data.py
```

# Answer to Reflections

### Abstraction: *What did you choose to inspect, and why?*

***Answer:*** In this exercise, I inspected various data quality indicators such as completeness of attributes and validity of coordinates. This is an important step so as to avoid problems in the output such as points not rendering due to missing lat/long values and/or to curate and early detection of "bad numbers" (i.e., longitude values going past 180°).

### Representation: *What assumptions are you making about the CSV and coordinates?*
***Answer:*** The assumptions about the CSV values and coordinates are they represent discreet locations in and around UP Diliman diliman campus, represented as points.

### Responsibility: *What should the script check automatically vs what a human should check?*
***Answer:*** The script should be able to automatically check data errors such as null or blank coordinate fields and coordinates that are out of bounds such as latitude values outside [-90, 90] and longitude outside [-180, 180]. The things that a human should check now are reviewing, for example, mirrored coordinates (inputting -12 instead of 12) or logical mismatch such as location saying UP Diliman but the coordinate pair is in another area.

### Scale: *What problems might happen if the dataset becomes very large?*
***Answer:***  One problem I could think of would be visual clutter since the given lat/long range is very small, adding more unique points would make very close to each other. Another possible one is memory exhaustion if the computer RAM is not able to handle loading all of the data points into memory.