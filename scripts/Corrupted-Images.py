''' Checking for corrupted images in a directory.
This script will also detect partially corrupted images, for example images with 
black/grey/red pixels or bands. These images avoid the Image.verify() check but 
will get caught byt applying transformations.

Bear in mind that this script is substantially slower than just trying to open images but also superior'''

import os
from pathlib import Path
from PIL import Image


def check_corrupted(img_path):
    img = Image.open(os.path.join(dir_in, img_path))
    # this will verify that img is indeed an image, but won't check for corrupted images that load with partial corruptions eg. black pixels or bands.
    img.verify()
    img.close()
    img = Image.open(os.path.join(dir_in, img_path))
    # Partially corrupted images (eg. with black/grey/red bands) will produce an error during the transpose command.
    img.transpose(Image.FLIP_LEFT_RIGHT)
    img.close()


# path to the directory you want to  check
dir_in = r"C:\Users\Konpoul\Desktop\EDEN_Library\GitHub\eden_library_notebooks\eden_data\Tomato-240519-Healthy-zz-V1-20210225103740"

count = 0
for img_path in os.listdir(dir_in):
    if img_path.endswith('.JPG'):
        try:
            check_corrupted(img_path)
        except(IOError, SyntaxError)as e:
            print(f'Bad file : {img_path}')
            # Uncomment if you want to delete it automatically
            #os.remove( os.path.join(dir_in,img_path) )
            #print(f"Removed corrupted image {img_path}")
            count = count+1

print(f"Number of corrupted images : {count}")
