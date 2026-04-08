# Simple Python File Organizer
A lightweight script to clean up cluttered directories (like your Downloads folder) by automatically sorting files into categorized subfolders based on their extensions.

## Core Logic
Extension Sorting: Automatically groups images, documents, code, and archives.

Safety First: Skips existing directories and the script file itself to avoid loops.

Cross-Platform: Uses pathlib for consistent path handling on Windows, Linux, and macOS.

Zero Dependencies: Built entirely with Python standard libraries (shutil, os, pathlib).

# Setup and Usage
## 1.Clone the repository:

git clone https://github.com/EnzzoChacon/Folder-Automation.git
## 2.Configure the Path:
Open the script and update the source_path variable to point to the directory you want to organize:

Python
source_path = Path("C:/Users/YourName/Downloads")
## 3.Run the Script:

python organizer.py
## Requirements
Python 3.6 or higher.

No external libraries required (uses standard modules os, shutil, and pathlib).

## Customization
You can easily add new file types or change folder names by modifying the file_mapping dictionary:

Python
file_mapping = {
    "Media": [".mp4", ".mkv", ".mp3"],
    "Design": [".psd", ".ai", ".fig"]
}
