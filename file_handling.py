"""
=============================================================
TASK 1: Python File Handling & Automation
Author: Ronak | Alfido Tech Internship
Goal: File read/write, automation (rename/move/delete), exception handling
=============================================================
"""

import os
import shutil
import csv

def write_txt_file():
    try:
        with open("students.txt", "w") as f:
            f.write("Name, Age, City\n")
            f.write("Ronak, 20, Bikaner\n")
            f.write("Amit, 21, Jaipur\n")
            f.write("Priya, 22, Delhi\n")
        print("[✓] students.txt created successfully")
    except IOError as e:
        print(f"[✗] Error writing file: {e}")

def read_txt_file():
    try:
        with open("students.txt", "r") as f:
            content = f.read()
        print("\n[✓] File Content:")
        print("-" * 30)
        print(content)
    except FileNotFoundError:
        print("[✗] File not found! Run write_txt_file() first.")

def write_csv_file():
    try:
        with open("products.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Product", "Price", "Stock"])
            writer.writerow(["Laptop", 45000, 10])
            writer.writerow(["Mouse", 500, 50])
            writer.writerow(["Keyboard", 800, 30])
        print("[✓] products.csv created successfully")
    except Exception as e:
        print(f"[✗] CSV Write Error: {e}")

def read_csv_file():
    try:
        with open("products.csv", "r") as f:
            reader = csv.reader(f)
            print("\n[✓] CSV File Content:")
            print("-" * 35)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("[✗] CSV file not found!")

def rename_file():
    try:
        os.rename("students.txt", "students_backup.txt")
        print("\n[✓] File renamed: students.txt → students_backup.txt")
    except FileNotFoundError:
        print("[✗] Original file not found for renaming!")
    except PermissionError:
        print("[✗] Permission denied! Cannot rename file.")

def move_file():
    try:
        os.makedirs("backup_folder", exist_ok=True)
        shutil.move("students_backup.txt", "backup_folder/students_backup.txt")
        print("[✓] File moved to backup_folder/")
    except FileNotFoundError:
        print("[✗] File to move not found!")
    except Exception as e:
        print(f"[✗] Move Error: {e}")

def delete_file():
    try:
        os.remove("products.csv")
        print("[✓] products.csv deleted successfully")
    except FileNotFoundError:
        print("[✗] File already deleted or not found!")
    except PermissionError:
        print("[✗] Cannot delete - file is in use or no permission.")

def append_to_file():
    try:
        with open("backup_folder/students_backup.txt", "a") as f:
            f.write("Sneha, 23, Mumbai\n")
        print("[✓] New record appended to students_backup.txt")
    except FileNotFoundError:
        print("[✗] File not found for appending!")

if __name__ == "__main__":
    print("=" * 50)
    print("  TASK 1: File Handling & Automation Demo")
    print("=" * 50)
    write_txt_file()
    read_txt_file()
    write_csv_file()
    read_csv_file()
    rename_file()
    move_file()
    append_to_file()
    delete_file()
    print("\n[✓] All file operations completed successfully!")
    print("=" * 50)