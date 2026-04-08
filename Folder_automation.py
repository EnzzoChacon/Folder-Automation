import os
import shutil
from pathlib import Path

source_path = Path("C:/Users/Enzzo/Downloads")

file_mapping = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Programming": [".py", ".gd", ".html", ".css", ".js", ".json", ".cpp", ".c"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".msix"]
}

def organize_folder(directory):
    if not directory.exists():
        print(f"Error: {directory} not found.")
        return

    current_script = Path(__file__).name

    for item in directory.iterdir():
        if item.is_dir() or item.name == current_script:
            continue
            
        file_extension = item.suffix.lower()
        
        for folder_name, extensions in file_mapping.items():
            if file_extension in extensions:
                dest_folder = directory / folder_name
                dest_folder.mkdir(exist_ok=True)
                
                try:
                    shutil.move(str(item), str(dest_folder / item.name))
                    print(f"MOVED: {item.name} -> {folder_name}")
                except Exception as e:
                    print(f"FAILED: {item.name} | {e}")
                break

if __name__ == "__main__":
    organize_folder(source_path)