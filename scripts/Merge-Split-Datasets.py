'''
Merge different datasets and split them into train-validation subsets in order to create the folder structure below:
main_folder
|---train
|    |--class_1
|    |--class_2
|    |...
|
|---val
|    |--class_1
|    |--class_2
|    |...

 WARNING: Original folders will become empty after this. If you want to keep original folders intact,
 use shutil.copy() instead of shutil.move
'''
import os
import random
import shutil


# Where you want the main folder to be
main_folder = '/main_folder/path'

# Create train and val folders that will host the data.
train_path = '/main_folder/path/train'
os.mkdir(train_path)
val_path = '/main_folder/path/val'
os.mkdir(val_path)

# Include all the different datasets/class names
classes = ['human', 'Tomato', 'Car']
num_classes = len(classes)  # we will need this later
for class_name in classes:
    # Path to source folders
    class_path = main_folder + class_name

    # Create subfolder for each class in validation folder
    class_val_path = val_path + os.path.sep + class_name
    os.mkdir(class_val_path)
    # Move original folder to train folder, created above
    class_train_path = train_path + os.path.sep + class_name
    shutil.move(class_path, train_path)

    # List of all files
    images = os.listdir(class_train_path)
    # Splitting randomly, choosing some files for validation.
    # Change ' *0.1 ' to whatever train-test split value you want
    valid_images = random.sample(images, (int(round(len(images)*0.1))))

    # Move validation images to validation folder
    for val_image in valid_images:
        shutil.move(class_train_path + os.path.sep + val_image,
                    class_val_path + os.path.sep + val_image)
        print("Moved ", val_image, " to validation images")
