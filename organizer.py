import os
import shutil
import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import json

working_directory = ""
organizer_configuration = {}


#reads the user configuration for organizer
def get_config():
    #get the global variable
    global organizer_configuration
    #open the file for reading
    with open('preferences.json', 'r') as open_file:
        #store the json contents in a dictionary
        organizer_configuration = json.load(open_file)


def open_directory():
    global working_directory
    fp = fd.askdirectory()
    if fp:
        working_directory = fp
    
