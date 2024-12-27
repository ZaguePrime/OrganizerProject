import os
import shutil
import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import json
import re

# working directory stores the path of the directory to organize, i.e: downloads
working_directory = ""
# this stores the dictionary form of the json preference, i.e key-value pairs
organizer_configuration = {}
# this is an array of filepaths created based on preferences
organized_paths = {}

# reads the user configuration for organizer
def get_config():
    global organizer_configuration
    with open('preferences.json', 'r') as open_file:
        organizer_configuration = json.load(open_file)

# opens the directory to work in and stores its path
# This works as expected
def open_directory():
    global working_directory
    fp = fd.askdirectory()
    if fp:
        working_directory = fp
        print(working_directory)

# create the organized directories
def create_paths():
    # Declare necessary files as global
    global organized_paths, working_directory, organizer_configuration
    # Loop through the json and create paths based on keys
    #Store the paths in the organized_paths dictionary
    for category in organizer_configuration.keys():
        organized_paths[category] = os.path.join(working_directory, category)
    
    # Now for each directory in the paths dictory, create the directory
    # Ensure that it is readable, writable and executable
    for directory in organized_paths.values():
        os.makedirs(directory, mode=0o777, exist_ok=True)

