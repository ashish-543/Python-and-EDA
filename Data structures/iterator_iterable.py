# Iterator
# Common data types store all the data in the memory
# Iterator is not like data types which behave as containers that stores values
# Iterator behaves like a machine that produces values one by one as long as you are asking for it
# Iterator doesnot create all the values at once, it creates values one-by-one only if asked
# Examples: iterator inside the for loop
# In the for loop, the iterator produces values one-by-one.

# Uses of iterators:
# 1. For looping
# 2. For bigdata, iterators are used which streams the data one-by-one instead of streaming all the data at once
#  and consuming high amount of memory. Hence, using iterators save memory

# 3. Speed, since iterators donot store the values in the memory and produce values only when asked, it increases the eficiency and speed


# Iterable
# Iterable is something that can be iterated
# Eg: lists, string etc
# Not iterable eg: integers, boolean values (True, False)

letters = ['a', 'b', 'c']
# Create a new list and add add the uppercase of each element of letters to that list

# new_list =[
#     letter.upper()
#     for letter in letters
# ]
# print(new_list) -> ['A', 'B', 'C']

# Without using list comprehension
new_list = []
for letter in letters:
    new_list.append(letter.upper())
    print(new_list)
# ['A']
# ['A', 'B']     
# ['A', 'B', 'C']    

# 1. enumerate
# It is an iterator that returns two values: position number and value
# enumerate(value) returns an iterator object
letters = ['a', 'b', 'c']
print(enumerate(letters)) # <enumerate object at 0x000001E9159F2C50>
print(list(enumerate(letters))) # [(0, 'a'), (1, 'b'), (2, 'c')]
# By default, the starting position is 0

# While using iterator in loops, no need to convert iterator object into list
# Use case: enumerate is used with loops to locate the position of bad values
for value, letter in enumerate(letters):
    print(f'{value} {letter}')
# 0 a
# 1 b
# 2 c
# To start the position from 1: for value, letter in enumerate(letters, start = 2)


# 2. reversed
print(reversed(letters)) # <list_reverseiterator object at 0x0000022152BE6380>
print(list(reversed(letters))) # ['c', 'b', 'a']


# 3. zip
# combines two list as ordered pairs if match is found
letters = ['a', 'b', 'c']
Numbers = [1, 2, 3]
print(zip(letters, Numbers)) # <zip object at 0x000001FCF8EAFAC0>
print(list(zip(letters, Numbers))) # [('a', 1), ('b', 2), ('c', 3)]
for letter, value in zip(letters, Numbers):
    print(letter, value)
# a 1
# b 2
# c 3


# 4. map
# map(function, iterable)
# To perform transformations on list, instead of using loops, map can be used to transform all the elements of a list
# You cannot use nested functions such as str.lower.strip inside map. Use lambda functions in such conditions
letters = ['a', 'b', 'c']
# convert the elements of list uppercase without using loop
print(map(str.upper, letters)) # <map object at 0x000001E2B52D6B00>
print(list(map(str.upper, letters))) # ['A', 'B', 'C']

# convert the given numbers into float without using loop
numbers = [1, 2, 3]
print(list(map(float, numbers))) # [1.0, 2.0, 3.0]

# Clean up the list by removing all the unwanted spaces using map
names = ['Harry ', ' brook ', 'george']
print(list(map(str.strip, names))) # ['Harry', 'brook', 'george']

for name in map(str.strip, names):
    print(name)
# Harry
# brook
# george

# 5. filter
# filter(function, iterable)
# This filters the data as per the function used

# Filter the given data 
letters = ['a', '', 'b', None, 'c', False]
filter(bool, letters)
print(list(filter(bool, letters))) # ['a', 'b', 'c']

# keep only the letters
items = ['sql', '555', 'python', '567']
print(list(filter(str.isalpha, items))) # ['sql', 'python']

for item in filter(str.isalpha, items):
    print(item)
# sql
# python

# only the numeric values
print(list(filter(str.isnumeric, items))) # ['555', '567']
