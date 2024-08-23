import os
import shutil
import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import json

#working directory stores the path of the directory to organize, i.e: downloads
working_directory = ""
#this stores the dictionary form of the json preference, i.e key-value pairs
organizer_configuration = {}
#this is an array of filepaths created based on preferences
organized_paths = {}

#reads the user configuration for organizer
def get_config():
    #get the global variable
    global organizer_configuration
    #open the file for reading
    with open('preferences.json', 'r') as open_file:
        #store the json contents in a dictionary
        organizer_configuration = json.load(open_file)

#opens the directory to work in and stores its path
def open_directory():
    #get the global variable
    global working_directory
    #ask for the directory
    fp = fd.askdirectory()
    #if not null just assign the value to the variable
    if fp:
        working_directory = fp

#create the organized directories
def create_paths():
    #get the global variable
    global organized_paths, working_directory, organizer_configuration
    #loop through and create the file paths
    for category in organizer_configuration.keys():
        organized_paths.append(os.path.join(working_directory, category))
    for directory in organized_paths():
        os.mkdir(directory, mode=0o777, exists_ok=True)

    
    
