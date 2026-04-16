import os

# 1. Getting the absolute path of files and folders
# Convert a relative file path into an absolute path (the full path from the root directory) based on the current working directory
print(os.path.abspath('another/path.py')) # D:\Python code\another\path.py

# 2. Splitting the base file and the path
path = os.path.abspath('another/path.py')
print(path.rsplit('\\', maxsplit = 1)) # rslpit -> splits from the right direction, two \\ since \ is an escape character
# ['D:\\Python code\\another', 'path.py']

splited_path = path.rsplit('\\', maxsplit = 1)
print('Path:', splited_path[0]) # Path: D:\Python code\another
print('FileName', splited_path[1]) # FileName path.py

# This splitting process can be done using os module
# After passing the absolute path, it automatically find the path and filename

# Getting the path to the folder 
print('Path:', os.path.dirname(path)) # Path: D:\Python code\another

# Getting the file
print('FileName:', os.path.basename(path)) # FileName: path.py

# 3. Checking if the file or folder exists
# Here path.py lies inside (another) folder in the pwd

print(os.path.isfile('path.py')) # False, since it exists inside another folder

print(os.path.isfile('another/path.py')) # True

# create another file path1.py inside another folder and check if that file already exists or not
if not os.path.isfile('another/path1.py'):
    print('File not present. Creating path1.py')

    with open('another/path1.py', 'w') as f:
        f.write('print(\'This is inside path1.py\')')
else:
    print('File already exists')


# Create a folder new_folder inside pwd and check if that folder already exists or not
if not os.path.isdir('new_folder'):
    print('No such folder. Creating new_folder')
    os.makedirs('new_folder')
else:
    print('Folder already exists')

