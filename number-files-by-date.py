import os
import time

dir_name = '/Applications/MAMP/htdocs/number-files-by-date/Test'

# Get list of all files only in the given directory
list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) )
# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files,
                        key = lambda x: os.path.getmtime(os.path.join(dir_name, x))
                        )
# Iterate over sorted list of files and print file path 
# along with last modification time of file 
for file_name in list_of_files:
    file_path = os.path.join(dir_name, file_name)
    timestamp_str = time.strftime(  '%m/%d/%Y :: %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path))) 
    print(timestamp_str, ' -->', file_name)    

