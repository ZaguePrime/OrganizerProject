import os
import shutil
import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import json

working_directory = ""
organizer_configuration = {}
organized_paths = {}
current_files = {}
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


    
