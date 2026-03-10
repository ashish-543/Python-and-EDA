# There are two types of data used in I/O
 # 1. Text: '12345' as a sequence of unicode chars
 # 2. Binary: 12345 as a sequence of bytes of its binary equivalent
# Hence, there are two types to deal with
 # 1. Text files: All program files are text files
 # 2. Binary files: Images, Music, videos, exe files

# How file I/O is done in most programming languages:
 # Open a file
 # Read/Write data
 # Close the file


# Writing to a file

# Case 1: If the file is not present
# f = open('file.txt', 'w') # f is the file handler object
# f.write('python')
# f.close()
# f.write('language') # ValueError: I/O operation on closed file.
# output inside the file: python

# Here opening the file moves the content of the file to the buffer i.e RAM as per the read/write instruction
# Closing a file removes the file from the buffer
# Inside the open, mention the path of the file if the created file is to be saved in different directory
# eg: D:\Python code\file.txt inside the open
# If only name is specified then the file is created in the same directory


# Write multiple lines
f = open('file.txt', 'w')
f.write('hello world')
f.write('python')
f.write('language')
f.close()
# Output in the file: hello worldpythonlangauge

f = open('file.txt', 'w')
f.write('hello word')
f.write('\npython')
f.write('\nlanguage')
f.close()
# hello word
# python
# language

# Case 2: If the file is already present
f = open('file.txt', 'w')
f.write('new')
f.close()
# output: new


# Adding lines at the end in the exiting file: a mode
f = open('file.txt', 'a')
f.write('\nyear')
f.close()
# new
# year


# Adding multiple lines using writelines
lines = ['hello', '\nworld', '\nthis', '\nis', '\npython']
f = open('file.txt', 'w')
f.writelines(lines)
f.close()
# hello
# world
# this
# is
# python


# Reading data from files
 # Reading data all at once
f = open('file.txt', 'r')
data = f.read()
print(data)
print(type(data))
f.close()
# hello
# world
# this
# is
# python
# <class 'str'>


# Reading upto 10 characters
f = open('file.txt', 'r')
data = f.read(10) # \n is also counted as a character
print(data)
f.close()
# hello   
# worl

# Reading lines of data using readline()
# readline is used when the file is very big so it loads the data line by line to save the memory of the ram
f = open('file.txt', 'r')
print(f.readline())
print(f.readline())
f.close()
# hello

# world

# Here the space is because print and readline both are newline functions so to solve this problem use end = '' in the print function

f = open('file.txt', 'r')
print(f.readline(), end = '')
print(f.readline(), end = '')
f.close()
# hello
# world


# Reading entire file using readline
# This code is widely used to print entirety of the data without knowing the actual number of lines in the file
f = open('file.txt', 'r')
while True:
    data  = f.readline()
    if data == '':
        break
    else:
        print(data, end ='')
f.close()
# hello
# world
# this
# is
# python

# This can also be done using 
with open('file.txt', 'r') as f:
    for lines in iter(lambda: f.readline(), ''): # iter(function, stop_value) or iter(number)
        print(lines, end = '')
# hello
# world
# this
# is
# python


#--------------------------------------------------------------------------------------------------------------------
# File handling using with -> Recommended and most widely used method
# with closes the file after the completion of execution without using close()

with open('file.txt', 'w') as f:
    f.write('This is with')
# output inside the file: This is with

# Now if any operations is done after the with then it throws error
with open('file.txt', 'w') as f:
    f.write('\nError example')
print(f.read()) # ValueError: I/O operation on closed file.


# Writing multiple lines using with
lines = ['hello', '\nworld', '\nthis', '\nis', '\npython']
with open('file.txt', 'w+') as f:
    f.writelines(lines)
# hello
# world
# this
# is
# python

# Reading data using with
with open('file.txt', 'r') as f:
    print(f.read())
# hello
# world
# this
# is
# python


#---------------------------------------------------------------------------------------------------------------------
# Moving within a file
# Print the first 10 character and then next 10 characters
with open('file.txt', 'r') as f:
    print(f.read(10)) # [h e l l o \n w o r l] -> the file poniter moves to the 11th character after reading 10 characters
    print(f.read(10)) # [d \n t h i s \n i s \n]
# hello
# worl
# d
# this
# is
#

# benefit -> to load a big file in memory
big_L = [
    f'{i}python '
    for i in range(100)
]
print(big_L) # ['python', 'python', 'python',.......]

with open('big_list.txt', 'w') as f:
    f.writelines(big_L)

# Processing only 10 characters at once
with open('big_list.txt', 'r') as f:
    chunk_size = 10
    chunk = f.read(chunk_size)
    while chunk:
        print(chunk, end = '*')
        chunk = f.read(chunk_size)
# 0python 1p*ython 2pyt*hon 3pytho* ..................

# This can also be done using iter()
with open('big_list.txt', 'r') as f:
    chunk_size = 10
    for chunk in iter(lambda: f.read(chunk_size), ''):
        print(chunk, end = '*') # 0python 1p*ython 2pyt*hon....................


#---------------------------------------------------------------------------------------------------------------------
# seek and tell function

# tell -> returns the current position of file pointer 
# Initially tell() returns 0 for the first character and after moving, it returns the position of next character to be processed
with open('file.txt', 'r') as f:
    print(f.read(10))
    print(f.tell())
# hello
# worl
# 11 # It is due to the /r that might be present in \n character so the answer should be 10


with open('file.txt', 'w') as f:
    f.write('saasa daaddd waewe ddad daadadd')

with open('file.txt', 'r') as f:
    print(f.read(10))
    print(f.tell())
# saasa daad
# 10


# seek -> moves the position of file pointer as per the instruction
# print first 10 characters twice
with open('file.txt', 'r') as f:
    print(f.read(10)) 
    f.seek(0)
    print(f.read(10))
# saasa daad
# saasa daad

# seek during write
with open('file.txt', 'w') as f:
    f.write('Hello world')
    f.seek(0)
    f.write('X')
# Xello world
# This is because you are performing two write operations on already opened file
# First the file opened in write mode clears the content of the file then write operation is performed
# On the same opened file after moving the file pointer using seek and performing write doesnot clear the whole content
# It is because write operation is performed on already open file
# So performing multiple write operations on already opened file doesnot clear the content of the file


