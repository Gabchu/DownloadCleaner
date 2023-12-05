import os
import numpy as np
import shutil


def clean_desktop(path):
    if not os.path.exists(path):
        # If path does not exist, print folder doesn't exist
        print(f"Folder does not exist: {path}")
        return

    # List all the files
    files = os.listdir(path)

    filetype = {
        'Documents': ['doc', 'docx', 'xlsm', 'xls', '.PDF', 'xlsx', 'pdf', 'csv', 'pptx', 'epub'],
        'Codes': ['php', 'htm', 'ipynb'],
        'Images': ['drawio', 'svg', 'jpg'],
        'Executables': ['exe', 'msi', 'ppk'],
        'Archives': ['zip'],
        'Others': []
    }

  # Function to look at unique extensions
    # extensions = set()

    # for file in files:
    #     name, ext = os.path.splitext(file)
    #     extensions.add(ext.encode('utf-8'))

    # print(extensions)

    for category in filetype:
        categoryPath = os.path.join(path, category)
        if not os.path.exists(categoryPath):
            os.mkdir(categoryPath)

    for file in files:
        filePath = os.path.join(path)


clean_desktop(r"C:\Users\terre\Downloads")
