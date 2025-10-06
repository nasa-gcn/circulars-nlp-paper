"""
GCN Circulars: Extract + Plot Yearly Histogram
-----------------------------------------------
1. Extract GCN circular JSONs from tar.gz.
2. Collect submission years.
3. Plot a clean yearly histogram.
4. Save figure as high-quality PDF.
"""

import tarfile
import os
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Extract GCN JSONs
# -----------------------------
tar_path = "../data/archive_2025.json.tar.gz"
extract_dir = "../data/all_gcn_circulars"

if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

with tarfile.open(tar_path, "r") as tar:
    tar.extractall(path=extract_dir)

json_dir = os.path.join(extract_dir, "archive.json")
files = sorted(
    [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith(".json")]
)

print(f"Number of Circular JSONs: {len(files)}")
print(f"First JSON path: {files[0]}")

# -----------------------------
# Step 2: Load Circular Data
# -----------------------------
time_stamps = []
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        data = json.load(file)
        time_stamps.append(
            datetime.datetime.fromtimestamp(int(data["createdOn"]) / 1000.0)
        )

# -----------------------------
# Step 3: Extract Years
# -----------------------------
years = np.array([ts.year for ts in time_stamps])
start_year, end_year = years.min(), years.max()
bins = np.arange(start_year - 0.5, end_year + 1.5, 1)

# -----------------------------
# Step 4: Plot Histogram
# -----------------------------
plt.figure(figsize=(10, 6))
counts, _, _ = plt.hist(
    years, bins=bins, rwidth=0.8, edgecolor="white", alpha=0.9
)

plt.xlabel("Year", fontsize=18)
plt.ylabel("GCN Circulars Published Per Year", fontsize=18)
# plt.title("GCN Circulars Published Per Year", fontsize=18, fontweight="bold", pad=15)

# X-ticks
plt.xticks(np.arange(start_year, end_year + 1, 2), fontsize=14, rotation=45)
plt.yticks(fontsize=14)

# Vertical lines + annotations
# plt.plot([2017.6, 2017.6], [0, max(counts) * 1.05], linestyle='--', color='C2')
# plt.annotate('LIGO/Virgo O2: GW170817', xy=(2017.8, max(counts) * 0.9), color='C2', fontsize=12)

plt.plot([2023.3, 2023.3], [0, max(counts) * 2.05], linestyle="--", color="C1")
plt.annotate(
    "Circular Migration to New GCN",
    xy=(2015.0, max(counts) * 1.0),
    color="C1",
    fontsize=15,
)

# Y-axis limit
plt.ylim(0, 3500)

# Remove grid for cleaner look
plt.grid(False)

# Tight layout & save
plt.tight_layout()
output_pdf = "../figures/GCN_Circulars_Per_Year.pdf"
plt.savefig(output_pdf, bbox_inches="tight")
plt.show()

print(f"Saved high-quality PDF as {output_pdf}")
