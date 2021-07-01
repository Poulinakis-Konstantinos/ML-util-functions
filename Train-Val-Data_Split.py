'''
Splits a folder containing all dataset images in train and validation folders. 
Also splits the folder containing the labels in the same way, creating val_label and train_label folders.
Labels and images are supposed to be in different folders. If they are not use utility script Separate-Images-from-Labels.py
'''

import os
import random
import shutil

# Path to source folders
images_path = ".../images/train"
labels_path = ".../labels/train"

# Path to validation folder. [Create if they don't exist]
img_val_path   = ".../images/val"
label_val_path = ".../labels/val"
val_paths = [img_val_path, label_val_path]
for val_path in val_paths:
	if not os.path.exists(val_path):
		os.makedirs(val_path)
		print("Directory '%s' created" %val_path)
	else:
		print("Directory '%s' already exists, continuing..." %val_path)



# List of all original files
images = os.listdir(images_path)
labels = os.listdir(labels_path)

# Splitting randomly, choosing some files for validation.
split_fraction = 0.2 #Change to whatever train-test split value suits you
valid_images = random.sample(images,(int(round(len(images) * split_fraction)))) 

# Splitting labels in the same way 
valid_labels =[]
for name in valid_images :
	print("Val image:", name)
    # If your annotations are not .txt type change to the appropriate extension. This is for yolo annots
	valid_labels.append(name.split('.')[0] + '.txt')


# Move validation images to validation folder
for val_image in valid_images:
	shutil.move( images_path + os.path.sep + val_image,
				 img_val_path + os.path.sep + val_image)
	print("Moved ",val_image," to validation images" )

# Move validation labels to validation folder
for val_label in valid_labels:
	shutil.move( labels_path + os.path.sep + val_label, 
				 label_val_path + os.path.sep + val_label)
	print("Moved ", val_label, " to validation labels")