import os
import json
import pandas as pd
import matplotlib.pyplot as plt

# File paths
DATA_PATH = "../data/points.csv"
OUTPUT_DIR = "../output"
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "summary.json")
PLOT_PATH = os.path.join(OUTPUT_DIR, "preview.png")

# A. Read the CSV file
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"Error: The file {DATA_PATH} was not found.")
    print("Please ensure the file \"points.csv\" exists in the specified path.")
    exit(1)

print("=== DATA INSPECTION REPORT ===")

# B. Inspect the data
num_rows, num_cols = df.shape

print("\n Basic Information")
print("------------------")
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
print(f"Column names: {list(df.columns)}")


