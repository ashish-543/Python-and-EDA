import shutil
import os

# The are multiple files inside (another) folder
# Copy all these files into another folder named new_folder

print(os.listdir('another')) # ['path.py', 'path.txt', 'path1.py']
print(os.listdir('new_folder')) # []

# Now copy all the files from another to new_folder
files = os.listdir('another')
destination = 'new_folder'

for file in files:
    source = os.path.join('another', file) # another\path.py.......
    shutil.copy(source, destination)


# Now write the same code for copying into new_folder1. Here new_folder1 doesnot exist
destination = 'NewFolder1'
os.makedirs('NewFolder1')
for file in files:
    source = os.path.join('another', file)
    shutil.copy(source, destination) # Here, the folder should exist beforehand because it can only create files


# copying only the text file from another folder into images folder
destination = 'images'
for file in files:
    if file.endswith('txt'):
        source = os.path.join('another', file)
        shutil.copy(source, destination)

#------------------------------------------------------------------------------------------------------------------

# Copying entire folders
# There is a folder images in the pwd, copy this folder into another folder named images1. Here images1 doesnot exist
shutil.copytree('images', 'images1') # Here it automatically creates images1 
# If the file already exists then it will throw FileExistsError error
# So the destination folder should not exist beforehand

#------------------------------------------------------------------------------------------------------------------

# Deleting folders
# It deleted the folder even if it is not empty
# The folders are permanently deleted i.e deleted folders are not inside recycle bin

# Delete a folder Newfolder which is not empty
print()
print(os.listdir('NewFolder1')) # ['path.py', 'path.txt', 'path1.py']
shutil.rmtree('NewFolder1')
