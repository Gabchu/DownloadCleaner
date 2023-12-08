import os
import shutil
import sys
sys.stdout.reconfigure(encoding='utf-8')


def clean_desktop_downloads(folder_path):
    # Make sure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return

    # List all files in the folder
    files = os.listdir(folder_path)

    # Define categories for file types
    file_types = {
        'Documents': ['doc', 'docx', 'xlsm', 'xls', '.PDF', 'xlsx', 'pdf', 'csv', 'pptx', 'epub'],
        'Codes': ['php', 'htm', 'ipynb'],
        'Images': ['drawio', 'svg', 'jpg'],
        'Executables': ['exe', 'msi', 'ppk'],
        'Archives': ['zip'],
        'Others': []
    }

    # Create folders for each category if they don't exist
    for category in file_types.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Move files to their respective folders based on file type
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            for category, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    new_path = os.path.join(folder_path, category, file)
                    shutil.move(file_path, new_path)
                    print(f"Moved {file} to {category} folder.")
                    break
            else:
                # If the file doesn't match any category, move it to the 'Others' folder
                new_path = os.path.join(folder_path, "Others", file)
                shutil.move(file_path, new_path)
                print(f"Moved {file} to Others folder.")


if __name__ == "__main__":
    # Change this path to the location of your desktop downloads folder
    desktop_downloads_folder = r"C:\Users\terre\Downloads"

    clean_desktop_downloads(desktop_downloads_folder)
