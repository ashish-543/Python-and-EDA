# Getting current working directory
import os


# 1. Getting current working directory: Current Working Folder
os.getcwd()
print(os.getcwd()) # D:\Python code

#----------------------------------------------------------------------------------------------------------

# 2.  Listing all the directories 
print(os.listdir()) # Lists all the files in the current directory

print()

# To get the list of files from other directory, mention the path of that directory
print(os.listdir('\Python code'))


# There is another folder inside Python code called another folder that contains python 1.py
# To get this, copy the whole path of that folder
# In the path, \a is the escape character so \\ is used 
print(os.listdir('D:\Python code\\another folder')) # ['python 1.py']

print(type(os.listdir('D:\Python code\\another folder'))) # <class 'list'>
# It returns a list of files

# You can get the list of files of any folder from any location

#----------------------------------------------------------------------------------------------------------

# 3. Creating files 
# Make a folder named new folder 
os.mkdir('new') # this makes a new folder new inside th curent directory
# If the file directory already exists then new directory with the same name cannot be created

# You can also mention the whole path to make directories in the specific locations
os.mkdir('D:\\another') # This makes new folder named another in the local disc D

# so using mkdir, you can make directories on any location
# mkdir is only used to create folders but it cannot create files such as python files 


# Creating files using makedirs
# makedirs is similar to mkdir but using makedirs we can make multiple folders
# Also in case of mkdir, the root folder must exist eg: os.mkdir('D:\Python code\new'), Python code must exist to create new
# But in case of makedirs, if the root directory doesnot exist, it automatically creates all the mentioned folders

os.makedirs('new\\another_new\yet_another')
# This creates yet_another folder inside another_new folder inside new folder
# Here all of these folders donot exist

os.makedirs('new\\another_new\yet_another', exist_ok = True)
# If exist_ok = True is used then it ignores the upper code if the folder already exists
# i.e if the folder already exists then nothing is done and it doesnot raise any FileExistsError exception

#----------------------------------------------------------------------------------------------------------

# 4. Joining paths
print(os.path.join('Python code', 'new')) # Python code\new
# It returns path after joining the names of the directories mentioned
# The directories donot have to exist. It simply joins whatever is mentioned and returns the path

# Create folder 2 inside folder 1 inside new folder using join inside the current directory
print(os.path.join('new', 'folder1', 'folder2')) # new\folder1\folder2
os.makedirs(os.path.join('new', 'folder1', 'folder2'), exist_ok = True)


# Now make the same directory structure inside the local disc D
print(os.path.join('D:\\', 'new', 'folder1', 'folder2')) # D:\new\folder1\folder2
os.makedirs(os.path.join('D:\\', 'new', 'folder1', 'folder2'), exist_ok = True)

#----------------------------------------------------------------------------------------------------------

# 5. Deleting files 
# os.remove() can only delete files but not folders

# There is a file called delete.py in the current directory, delete this file
os.remove('delete.py') # File deleted

# There is a folder called delete in the working directory inside which there is a file file.py, delete this file
os.remove(r'delete\file.py') # Since \ is a special character, use r'' where r means raw string

# there is a file python 1.py inside (another folder) which is inside working directory
# you are inside python 1.py and you have to delete a file random.py which is inside working directory which is 1 step above you
# so from python 1.py, remove ramdom.py which is 1 step above your current position in the directory hierarchy
os.remove(r'..\random.py')
# Here .. is used to move 1 step above your current position
# The relative file position is based on where the code is actually executed not the file position
# In our case, the code runs from python code regardless of the position of file inside another folder
# so using .. is not posible as it will throw error
# It is because __pycache__ is inside python code not another folder

# Deleteing files from anywhere using the absolute path
# There is a tect file one.txtin the folder new1 inside the D:, delete this file
os.remove(r'D:\new1\one.txt')
# This also does the same thing os.remove('D:\\new1\\one.txt')
# If r is not used then \\ have to be used inplace of \

# You can also use / instead of \ and it work the same
os.remove(r'D:/new1/one.txt')

#----------------------------------------------------------------------------------------------------------

# 6. Renaming files and folders

# there is file random.py in the current directory, rename it to random1.py
os.rename('random.py', 'random1.py') # Since the file is in current directory, no need to mention the full path

# there is s file python 1.py inside another folder in the current directory, rename it to python1.py
os.rename('another folder\\python 1.py', 'python1.py')
# This will rename the file but the renamed file will be moved to the current working directory instead of its previous location 
# which was inside (another folder).
# This is because python expects full path of the file. Since the new renamed file path is python.py
# which is understood as current_working_directory\python.py 
# So full file path instead of just name needs to be given in case of files that are present in another folder
os.rename('another folder/python 1.py', 'another folder/python1.py')

# There is a folder new in the current directory, rename it to news
os.rename('new', 'news')
# Even after renaming the folder, the directory hierarchy remains the same

# There is folder1 inside news folder in the current working directory, rename it to folder_one
os.rename('news/folder1', 'news/folder_one')

#----------------------------------------------------------------------------------------------------------

# 7. Deleting folders
# rmdir deletes a single empty folder
# removedirs removes all the empty folders 

# there is a empty folder delete inside the current working directory, delete this folder
os.rmdir('delete')

# there is folder2 inside folder1 inside new inside current working directory, delete all these folders
# os.rmdir('new') # This cannot delete multiple folders
os.removedirs('new/folder1/folder2')
# All the folders should be mentioned 

# In case of non folders, first the folders should be empties
# Inside pwd, there is (another folder) inside which there are two files, delete this folder
print(os.listdir('another folder')) # ['python1.py', 'python2.py']
# os.rmdir('another folder') # OSError: [WinError 145] The directory is not empty: 'another folder'

files = os.listdir('another folder')
for file in files:
    print(os.path.join('another folder', file))
    os.remove(os.path.join('another folder', file)) 
# another folder\python1.py
# another folder\python2.py
# Here the another folder is empty and now it can be deleted

os.rmdir('another folder')

#----------------------------------------------------------------------------------------------------------
# 8. Changing present working directory

print(os.getcwd()) # D:\Python code

# Read a file named path.txt inside folder named another inside pwd

with open('another/path.txt', 'r') as f:
    print(f.read()) # This is inside path.txt

# Here the cwd is:
print(os.getcwd()) # D:\Python code

# We can change the current working directory to another folder
os.chdir('another')
print(os.getcwd()) # D:\Python code\another

# So the file reading code becomes
with open('path.txt', 'r') as f: # This is inside path.txt
    print(f.read())


# Now to move one step above in the hierarchy
os.chdir('..')
print(os.getcwd()) # D:\Python code

# Now move to folder2 which is inside folder1 which is inside new inside pwd
os.chdir('new/folder1/folder2')
print(os.getcwd()) # D:\Python code\new\folder1\folder2

# Now to move back to Python code
os.chdir('../../..')
print(os.getcwd()) # D:\Python code












