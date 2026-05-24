"""
=============================================================
TASK 3: Data Analysis with Pandas
Author: Ronak | Alfido Tech Internship
=============================================================
"""

import pandas as pd
import numpy as np

def create_dataset():
    data = {
        "StudentID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        "Name":      ["Ronak", "Amit", "Priya", "Sneha", "Raj",
                      "Kavya", "Deepak", "Neha", "Vikram", "Anjali"],
        "Math":      [85, 92, 78, 45, 88, 95, 60, 72, 55, 90],
        "Science":   [90, 88, 82, 50, 75, 98, 65, 68, 48, 85],
        "English":   [75, 80, 88, 60, 70, 85, 72, 78, 62, 92],
        "City":      ["Bikaner", "Jaipur", "Delhi", "Mumbai", "Pune",
                      "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad"],
        "Attendance":[92, 88, 95, 60, 78, 100, 72, 85, 55, 96]
    }
    df = pd.DataFrame(data)
    return df

def explore_data(df):
    print("\n" + "=" * 55)
    print("  SECTION 2: Basic Data Exploration")
    print("=" * 55)
    print("\n[1] First 5 rows of dataset:")
    print(df.head())
    print("\n[2] Dataset Shape (rows, columns):", df.shape)
    print("\n[3] Column Names:", list(df.columns))
    print("\n[4] Data Types of each column:")
    print(df.dtypes)
    print("\n[5] Basic Statistics:")
    print(df.describe())

def clean_data(df):
    print("\n" + "=" * 55)
    print("  SECTION 3: Data Cleaning")
    print("=" * 55)
    df_dirty = df.copy()
    df_dirty.loc[2, "Math"] = np.nan
    df_dirty.loc[5, "Science"] = np.nan
    print("\n[1] Missing Values Before Cleaning:")
    print(df_dirty.isnull().sum())
    df_dirty["Math"] = df_dirty["Math"].fillna(df_dirty["Math"].mean())
    df_dirty["Science"] = df_dirty["Science"].fillna(df_dirty["Science"].mean())
    print("\n[2] Missing Values After Cleaning:")
    print(df_dirty.isnull().sum())
    df_dirty = df_dirty.drop_duplicates()
    print("\n[3] Duplicates removed. Final shape:", df_dirty.shape)
    return df_dirty

def analyze_data(df):
    print("\n" + "=" * 55)
    print("  SECTION 4: Data Analysis")
    print("=" * 55)
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    df["Average"] = np.round(df["Total"] / 3, 2)

    def assign_grade(avg):
        if avg >= 90:   return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        else:           return "F"

    df["Grade"] = df["Average"].apply(assign_grade)
    print("\n[1] Student Results Table:")
    print(df[["Name", "Math", "Science", "English", "Total", "Average", "Grade"]].to_string(index=False))
    top = df.loc[df["Average"].idxmax()]
    print(f"\n[2] Top Performer: {top['Name']} with Average = {top['Average']}")
    print("\n[3] Subject-wise Class Average (via NumPy):")
    for subject in ["Math", "Science", "English"]:
        avg = np.mean(df[subject])
        print(f"    {subject}: {avg:.2f}")
    print("\n[4] Grade Distribution:")
    print(df["Grade"].value_counts())
    passed = df[(df["Math"] >= 50) & (df["Science"] >= 50) & (df["English"] >= 50)]
    print(f"\n[5] Students who passed all subjects: {len(passed)}/{len(df)}")
    print(passed[["Name", "Math", "Science", "English"]].to_string(index=False))
    df_sorted = df.sort_values("Average", ascending=False)
    print("\n[6] Class Rank (sorted by Average):")
    df_sorted["Rank"] = range(1, len(df_sorted) + 1)
    print(df_sorted[["Rank", "Name", "Average", "Grade"]].to_string(index=False))
    return df

def export_results(df):
    try:
        df.to_csv("student_results.csv", index=False)
        print("\n[✓] Results exported to student_results.csv")
    except Exception as e:
        print(f"[✗] Export Error: {e}")

if __name__ == "__main__":
    print("=" * 55)
    print("  TASK 3: Data Analysis with Pandas & NumPy")
    print("=" * 55)
    df = create_dataset()
    explore_data(df)
    df = clean_data(df)
    df = analyze_data(df)
    export_results(df)
    print("\n[✓] Data Analysis Completed Successfully!")