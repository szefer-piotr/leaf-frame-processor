import glob

# Get jpeg files
jpeg_files = glob.glob("data/raw/*.jpg")

print(jpeg_files[:10])

# Get the tabular data

# Extract phot names as IDs in the tabular data

# Extract data from tabular files and attach path to jpeg as a column in the table.