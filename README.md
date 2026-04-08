## File Organizer
This Python script automates the organization of files in a specific directory by moving them into subfolders based on their file extensions. It is designed to keep download folders or workspaces clutter-free without manual intervention.

## Features
Automatic Categorization: Sorts files into predefined categories like Images, Documents, Programming, Archives, and Executables.

Safety Checks: Automatically skips directories and the script itself to prevent recursive errors or accidental moves.

Collision Prevention: Uses pathlib for robust path handling across different operating systems.

Case Insensitivity: Extension matching works regardless of whether the file uses uppercase or lowercase letters.

## How it Works
The script iterates through every file in the target directory. It extracts the file extension and compares it against a dictionary of mapped categories. If a match is found:

It checks if the destination subfolder exists.

It creates the folder if necessary.

It moves the file to its new location and logs the action in the console.

## Setup and Usage
## 1.Clone the repository:

Bash
git clone https://github.com/yourusername/file-organizer.git
## 2.Configure the Path:
Open the script and update the source_path variable to point to the directory you want to organize:

Python
source_path = Path("C:/Users/YourName/Downloads")
## 3.Run the Script:

Bash
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
