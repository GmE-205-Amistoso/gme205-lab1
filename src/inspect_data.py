import os
import json
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------
# File paths
# ----------------------
DATA_PATH = "../data/points.csv"
OUTPUT_DIR = "../output"
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "summary.json")
PLOT_PATH = os.path.join(OUTPUT_DIR, "preview.png")

# ----------------------
# A. Read the CSV file
# ----------------------
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"Error: The file {DATA_PATH} was not found.")
    print("Please ensure the file \"points.csv\" exists in the specified path.")
    exit(1)

print("=== DATA INSPECTION REPORT ===")

# ----------------------
# B. Inspect the data
# ----------------------
num_rows, num_cols = df.shape

print("\nBasic Information")
print("------------------")
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
print(f"Column names: {list(df.columns)}")

# ----------------------
# C. Data quality checks
# ----------------------
print("\nData Quality Checks")
print("-------------------")

# Check for missing values in the dataset
missing_values = df.isnull().sum()
if missing_values.any():
    print("Missing values per column:")
    print(missing_values)
else:
    print("No missing values detected.")

# Ensure required columns exist
required_columns = {"lon", "lat"}
if not required_columns.issubset(df.columns):
    missing = required_columns - set(df.columns)
    raise ValueError(f"Missing required columns: {missing}. Required: lon, lat")

# Invalid coordinates check
invalid_lon_mask = df["lon"].isna() | (df["lon"] < -180) | (df["lon"] > 180)
invalid_lat_mask = df["lat"].isna() | (df["lat"] < -90) | (df["lat"] > 90)

invalid_lon_count = int(invalid_lon_mask.sum())
invalid_lat_count = int(invalid_lat_mask.sum())

print(f"\nInvalid longitude values (missing or outside -180..180): {invalid_lon_count}")
print(f"Invalid latitude values (missing or outside -90..90): {invalid_lat_count}")

# ----------------------
# D. Bounding box (valid coordinates only)
# ----------------------
valid_mask = ~(invalid_lon_mask | invalid_lat_mask)
valid_df = df.loc[valid_mask].copy()

print("\nBounding Box")
print("----------------")

if len(valid_df) == 0:
    bbox = None
    print("No valid coordinate rows found. Bounding box cannot be computed.")
else:
    min_lon = valid_df["lon"].min()
    max_lon = valid_df["lon"].max()
    min_lat = valid_df["lat"].min()
    max_lat = valid_df["lat"].max()

    bbox = {
        "min_lon": float(min_lon),
        "max_lon": float(max_lon),
        "min_lat": float(min_lat),
        "max_lat": float(max_lat)
    }

    print(f"Min longitude: {min_lon}")
    print(f"Min latitude: {min_lat}")
    print(f"Max longitude: {max_lon}")
    print(f"Max latitude: {max_lat}")

    # ----------------------
# E. Save outputs 
# ----------------------

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Build summary dictionary
summary = {
    "file": DATA_PATH,
    "rows": int(num_rows),
    "columns": int(num_cols),
    "column_names": list(df.columns),
    "missing_values_per_column": {k: int(v) for k, v in missing_values.items()},
    "invalid_longitude_count": invalid_lon_count,
    "invalid_latitude_count": invalid_lat_count,
    "valid_coordinate_rows": int(len(valid_df)),
    "bbox": bbox
}

# Write summary to JSON file
with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print(f"\nSaved summary to {SUMMARY_PATH}")

# Save scatter plot of valid coordinates
plt.figure()
if(len(valid_df) == 0):
    plt.title("Preview Plot (No valid coordinates to plot)")
else:
    plt.scatter(valid_df["lon"], valid_df["lat"])
    plt.title("Point Preview (lon vs lat)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

plt.savefig(PLOT_PATH, dpi=150, bbox_inches="tight")
plt.close()

print(f"Saved scatter plot to: {PLOT_PATH}")
print("\n=== END OF REPORT ===")