import os

# To get the list of files and folders, we simply use listdir

# There is a root folder in the pwd, inside which there are 5 folders and inside each folder, there are various files
# So using listdir, we can only get the names of files and folders inside root folder 
# but we cannot get the files and subfolders inside those folders 

folders = os.listdir('root')
print(folders) # ['folder_1', 'folder_2', 'folder_3', 'folder_4', 'folder_5']
# Here, each of these folders contain several files which cannot be known using listdir

print(os.listdir('.')) # This returns the files and folders inside current directory


# To solve this problem, we use os.walk
print(os.walk('root')) # <generator object walk at 0x00000188EB3E01B0>
# Here, the output of os.walk() is a iterator object
print(list(os.walk('root')))
# This returns a list: [(curent directory, [folders], [files]),.........] until it covers the entire hierarchy
# the first hierarchy is the root node for which it returns: 
# [('root', ['folder_1', 'folder_2', 'folder_3', 'folder_4', 'folder_5'], [])


# So the os.walk() output has three values, each inside the tuple in the list i.e [(pwd, [folders], [files]), ...........]
for current, folders, files in os.walk('root'):
    print('Current Directory:',current)
    print('Folders:', folders)
    print('Files:', files)
    print('-' * 150)
    
# Output:
# Current Directory: root
# Folders: ['folder_1', 'folder_2', 'folder_3', 'folder_4', 'folder_5']
# Files: []
# -----------------------------------------------------------------------------------------------------------------------------
# Current Directory: root\folder_1
# Folders: []
# Files: ['file_1.txt', 'file_10.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt', 'file_5.txt', 'file_6.txt', 'file_7.txt',
#          'file_8.txt', 'file_9.txt', 'screenshot copy.png', 'screenshot.png']
# -----------------------------------------------------------------------------------------------------------------------------
# Current Directory: root\folder_2
# Folders: []
# Files: ['file_1.txt', 'file_10.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt', 'file_5.txt', 'file_6.txt', 'file_7.txt',
#          'file_8.txt', 'file_9.txt', 'screenshot.png']
# ------------------------------------------------------------------------------------------------------------------------------
# Current Directory: root\folder_3
# Folders: []
# Files: ['file_1.txt', 'file_10.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt', 'file_5.txt', 'file_6.txt', 'file_7.txt',
#          'file_8.txt', 'file_9.txt']
# ------------------------------------------------------------------------------------------------------------------------------
# and so on..................



# Iterating through each files and folders inside a directory
for pwd, folders, files in os.walk('root'):
    print('Current Directory:', pwd)
    
    for folder in folders:
        print('FolderName:', folder)

    for file in files:
        print('FileName:', file)
    print('*' * 50)

# Output
# Current Directory: root
# FolderName: folder_1
# FolderName: folder_2
# FolderName: folder_3
# FolderName: folder_4
# FolderName: folder_5
# **************************************************
# Current Directory: root\folder_1
# FileName: file_1.txt
# FileName: file_10.txt
# FileName: file_2.txt
# FileName: file_3.txt
# FileName: file_4.txt
# FileName: file_5.txt
# FileName: file_6.txt
# FileName: file_7.txt
# FileName: file_8.txt
# FileName: file_9.txt
# FileName: screenshot copy.png
# FileName: screenshot.png
# **************************************************
# and so on........................


# In above case, some of the files contain images. So copy all these these images into a new folder images inside pwd
# First check if images folder exists or not, and if it doesnot exists, create it.
import shutil

if not os.path.isdir('images'):
    os.makedirs('images')

for current, folders, files in os.walk('root'):
    print('Current Directory:', current)

    for folder in folders:
        print('FolderName:', folder)

    for file in files:
        print('FileName:', file)

        file_path = os.path.join(current, file)

        if file.endswith('png'):
            shutil.copy(file_path, 'images')

    print('*' * 100)

