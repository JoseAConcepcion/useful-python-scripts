import os
import shutil
import datetime
from collections import Counter

# Get the list of files in the current folder excluding directories
files = [file for file in os.listdir() if os.path.isfile(file)]

# Classify files by date and majority format
for file in files:
    modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    folder_name = modification_date.strftime("%y_%m_%d")
    
    # Filter files belonging to the same date
    same_date_files = [f for f in files if datetime.datetime.fromtimestamp(os.path.getmtime(f)).date() == modification_date.date()]
    
    # Count the number of files by format on the same date
    formats = [f.split('.')[-1] for f in same_date_files]
    majority_format = Counter(formats).most_common(1)[0][0]
    
    # Create the folder name with the majority format
    folder_name = f"{folder_name} (contains {majority_format})"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Copy the file to the corresponding folder if it doesn't exist
    if not os.path.exists(os.path.join(folder_name, file)):
        shutil.move(file, folder_name)

