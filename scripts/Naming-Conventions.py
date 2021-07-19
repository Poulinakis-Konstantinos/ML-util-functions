'''
Checking a folder with images for naming conventions such as the correct extension, lower_case/upper_case extensions.
Restructures file names so that the conventions are met.
'''
import os
from pathlib import Path


def extension_to_jpg(file_path):
    ''' Reformats the extension to the desired one eg. JPEG -> jpg '''
    file_name = file_path.split('.')[0]
    print(f"Changing file extension: Renaming file : {file_path}, to {file_name}.jpg")
    os.rename( os.path.join(dir_in, file_path) , os.path.join(dir_in,file_name+".jpg") )

def to_lower(file_path):
    ''' Changes the extension from Upper case letters to lower case letters '''
    file_name = file_path.split('.')[0]
    file_extension = file_path.split('.')[1]
    file_ext_low = file_extension.lower()
    print(f"File extension to lower case: Renaming file : {file_path}, to {file_name}.{file_ext_low}")
    os.rename( os.path.join(dir_in, file_path) , os.path.join(dir_in,file_name+'.'+file_ext_low) )

# path to the directory you want to  check
dir_in = r"PATH\TO\THE\DIRECTORY"

for img_path in os.listdir(dir_in):

    # Checking for jpeg extension
    if img_path.endswith('JPEG') or img_path.endswith('jpeg') :
        extension_to_jpg(img_path)
    # checking for upper case extension
    elif img_path.endswith('JPG'):
        to_lower(img_path)


        
