import os
import shutil
import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

working_directory = ""
# file_formats = {
#     "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic", ".ico", ".img"],
#     "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],
#     "Video": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
#     "Documents": [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp", ".rtf"],
#     "Compressed Files": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz"],
#     "Executables": [".exe", ".bat", ".sh", ".msi", ".app"],
#     "Data Files": [".csv", ".json", ".xml", ".yaml", ".yml", ".sql", ".db", ".mdb", ".sqlite"],
#     "Web Files": [".html", ".htm", ".css", ".js", ".php", ".asp", ".jsp"],
#     "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
#     "System Files": [".sys", ".dll", ".ini", ".log"],
#     "Miscellaneous": [".iso", ".dmg", ".torrent", ".md", ".epub", ".mobi"]
# }

# folder_creations = {category: False for category in file_formats}

# extension_to_category = {}
# for category, extensions in file_formats.items():
#     for extension in extensions:
#         extension_to_category[extension.lower()] = category

# categories = set(file_formats.keys())

# organized_paths = {}

# This function gets the file path that we want to organize
def open_file():
    #global variable for storing the working directory
    global working_directory, organized_paths
    #ask for the directory
    fp = fd.askdirectory()
    if fp:
        #if the directory is not null, set it
        working_directory = fp
        #basically create the sub-directories to organize into
        for path in file_formats.keys():
            organized_paths[path] = os.path.join(working_directory, path)

# This function is basically to check the contents of the selected directory
def scan_directory():
    #reference for the directory
    global working_directory
    #if a directory has not been selected
    if not working_directory:
        messagebox.showerror("Error", "Please select a directory first.")
        return

    try:
        #for each file in the directory
        for item in os.listdir(working_directory):
            #get its full path
            full_path = os.path.join(working_directory, item)
            #check if it is an individual file
            if os.path.isfile(full_path):
                #get the extentions
                _, ext = os.path.splitext(full_path)
                print(f"File: {item}, Extension: {ext}")
            #check if it is a directory
            elif os.path.isdir(full_path) and item not in categories:
                print(f"File: {item}, Extension: folder")
            #check if its a category
            elif os.path.isdir(full_path) and item in categories:
                folder_creations[item] = True
        create_folders()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_folders():
    global working_directory
    try:
        for folder_name in file_formats.keys():
            if not folder_creations[folder_name]:
                folder_path = os.path.join(working_directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                print(f"Created folder: {folder_path}")
        sort_directory()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create folders: {str(e)}")

def sort_directory():
    global working_directory, organized_paths, extension_to_category
    try:
        for item in os.listdir(working_directory):
            full_path = os.path.join(working_directory, item)
            if os.path.isfile(full_path):
                _, ext = os.path.splitext(full_path)
                category = extension_to_category.get(ext.lower(), "Miscellaneous")
                destination_folder = organized_paths.get(category, organized_paths["Miscellaneous"])
                destination_file_path = os.path.join(destination_folder, item)
                
                if os.path.exists(destination_file_path):
                    # Rename the file by appending a timestamp
                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    base_name, file_extension = os.path.splitext(item)
                    new_file_name = f"{base_name}_{timestamp}{file_extension}"
                    destination_file_path = os.path.join(destination_folder, new_file_name)
                
                shutil.move(full_path, destination_file_path)
            
            elif os.path.isdir(full_path) and item not in categories:
                # shutil.move(full_path, organized_paths["Miscellaneous"])
                continue
    except Exception as e:
        messagebox.showerror("Error", f"Failed to sort directory: {str(e)}")

window = Tk()

open_button = Button(text="Open Directory", command=open_file)
open_button.pack(pady=10)

organize_button = Button(text="Organize Directory", command=scan_directory)
organize_button.pack()

window.mainloop()
