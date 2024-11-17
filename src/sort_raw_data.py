import glob
import re

# Get jpeg files
jpeg_files = glob.glob("../data/raw/*.JPG")
xls_files = glob.glob("../data/raw/*.xls")

pattern = r"\(\d+\)"
image_files = [f for f in jpeg_files if not re.search(pattern, f)]

print(image_files[0], xls_files[0])

len(image_files), len(xls_files)

# Move jpegs to separate folder with images
import shutil
import os

source = 'data/raw'
image_dest = '../data/staged/images'
tabular_dest = '../data/staged/tabular'

os.makedirs(image_dest, exist_ok=True)
os.makedirs(tabular_dest, exist_ok=True)

for f in image_files:
    shutil.copy(f, image_dest)

for f in xls_files:
    shutil.copy(f, tabular_dest)