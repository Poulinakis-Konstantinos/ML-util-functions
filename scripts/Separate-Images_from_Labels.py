'''
Separates image files from label files (JPGs from TXTs) .

Reads folders that contains both .jpg and .txt files, defined in the list 'folders'.
Copies .jpg files to a destination folder .../images/train. 
Copies .txt files to a destination folder .../labels/train.

Use Train-Val-Data_Split.py script to split a dataset into train and validation subsets

|---dest_main_folder
|    |--images/train
|    |--labels/train

Original folders will remain intact. If you wish to permanently move all files from them use 
shutil.move() instead of shutil.copy() . 
'''

import os
import random
import shutil

# Define the folders that contain the original data you want to seperate
folder1 = '/path/to/1st/dataset/obj_train_data'
folder2 = '/path/to/2nd/dataset/obj_train_data'
# Put them in a list
folders = [folder1, folder2]

# Create the main folder to host the data eg. inside the YOLO folder. [Creates it only if it does not exist.]
dest_main_folder = '/destination/path/for/main/folder'
if not os.path.exists(dest_main_folder):
    os.makedirs(dest_main_folder)
    print("Directory '%s' created" % dest_main_folder)
else:
    print("Directory '%s' already exists, continuing..." % dest_main_folder)


# Create the train folder for images and labels
im_train_path = dest_main_folder + os.path.sep + 'images' + os.path.sep + 'train'
label_train_path = dest_main_folder + \
    os.path.sep + 'labels' + os.path.sep + 'train'
os.makedirs(im_train_path)
print("Directory '%s' created" % im_train_path)
os.makedirs(label_train_path)
print("Directory '%s' created" % label_train_path)

for folder in folders:
    for file in os.listdir(folder):
        # Move images to images/train directory
        if file.endswith('.jpg'):
            shutil.copy(folder + os.path.sep + file,
                        im_train_path + os.path.sep + file)
        # Move labels to images/train directory
        elif file.endswith('.txt'):
            shutil.copy(folder + os.path.sep + file,
                        label_train_path + os.path.sep + file)
