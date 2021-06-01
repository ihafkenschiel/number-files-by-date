#!/usr/bin/python

import os
import sys
import time

# For testing:
# dir_name = '/Applications/MAMP/htdocs/number-files-by-date/Test'

dir_name = ""
if len(sys.argv) == 2:
    dir_name = sys.argv[1]
    if os.path.isdir(dir_name):
        print("Adding tracks to folder: " + dir_name)
    else:
        print("ERROR: Not a folder: " + dir_name)
        quit()
else:
    while True:
        print("Enter full folder path:")
        dir_name = input()
        
        # remove single quotes around folder path if folder is draged to terminal
        if dir_name[0] == "'":
            dir_name = dir_name.strip("'")

        dir_name = dir_name.strip() # trim whitespace

        if os.path.isdir(dir_name):
            break

# Get list of all files only in the given directory
list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) )
# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files,
                        key = lambda x: os.path.getmtime(os.path.join(dir_name, x))
                        )
# Iterate over sorted list of files and print file path 
# along with last modification time of file 
count = 1
for file_name in list_of_files:
    file_path = os.path.join(dir_name, file_name)
    new_name = '%02d' % count + " - "  + file_name
    print(new_name)
    os.rename(dir_name + "/" + file_name, dir_name + "/" + new_name)
    count += 1

