# Problems with working in text mode
 # 1. Can't work with binary files like images
 # 2. Not good for other data types like: int/float/list/tuples

# Problem 1
# Working with binary file using text mode
with open('D:\Python code\Screenshot (90).png', 'r') as f:
    f.read() # UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 57: character maps to <undefined>
# Binary files cannot be opened in text mode

# Copying file
with open('D:\Python code\Screenshot (90).png', 'rb') as f:
    with open('screenshot.png', 'wb') as bf: # New file is created with same content as the above file
        bf.write(f.read()) 


# Problem 2
with open('file.txt', 'w') as f:
    f.write(5) # TypeError: write() argument must be str, not int
# # The data must be string for text files


with open('file.txt', 'w') as f:
    f.write('5') # Output in file: 5

with open('file.txt', 'r') as f:
    # print(f.read() + 5) # integer operations cannot be performed on strings
    print(int(f.read()) + 5) # 10

# Working with complex data types
dict = {
    'name': 'Aron',
    'age': 25,
    'country': 'Finland'
}
with open('file.txt', 'w') as f:
    # f.write(dict) # TypeError: write() argument must be str, not dict
    f.write(str(dict)) # output in the file: {'name': 'Aron', 'age': 25, 'country': 'Finland'}

with open('file.txt', 'r') as f:
    print(type(f.read()))
    f.seek(0)
    print(f.read()) # {'name': 'Aron', 'age': 25, 'country': 'Finland'}
    f.seek(0)
    print(type(f.read())) # <class 'str'>
    f.seek(0)
    print(dict(f.read())) # TypeError: 'dict' object is not callable
# Here once any data is stored in the text file, it is converted into string regardless of its previous data type
# The string data cannot be converted into complex data types like dict.


    
