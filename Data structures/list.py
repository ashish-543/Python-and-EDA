# Creating List
list1 = []
print(type(list1)) # list
print(bool(list1)) # Flase

list1 = [1,2,3,4,5]
print(bool(list1)) # True

list2 = ['a', 'b', 'c']
print(type(list2)) # list

# Mixed list
list3 = [1, 2, 'a', 'b']
print(type(list3)) # list

# Creating list using list()

list4 = list(range(5))
print(list4) # output: [0, 1, 2, 3, 4]
print(type(list4)) # list

list5 = list('python')
print(list5) # output: ['p', 'y', 't', 'h', 'o', 'n']
print(type(list5)) # list

name = 'harry'
list6 = list(name)
print(list6) # ['h', 'a', 'r', 'r', 'y']
print(type(list6)) # list


# Multi-dimensional list
# Use multuple [] inside []
# It is a better practice to use different line for each row in case of multi-dimensional lists
mlist = [[1, 2, 3],
         [4, 5, 6]]
print(type(mlist)) # list
print(mlist) # [[1, 2, 3], [4, 5, 6]]


# Python also supports lists having different number of elements in each row
mlist1 = [['a', 'b'],
          [1, 2, 3],
          [4, 5, 6, 7]]
print(mlist1) # [['a', 'b'], [1, 2, 3], [4, 5, 6, 7]]


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# Accessing lists (Indexing & Slicing)
# The first index is 0 and the last index is -1 regardless of the size of list.
lst = [1, 2, 3, 4, 5]
print(lst[0]) # 1
print(lst[-1]) # 5
print(lst[2]) # 3
print(lst[-3]) # 3

matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]
print(matrix[0][0]) # a
print(matrix[1][1]) # e
print(matrix[2][1]) # h
print(matrix[2][2]) # i
print(matrix[-1][-1]) # i
print(matrix[-1][-2]) # h

# Slicing
# Use : inside []. It is same as that of string. Behaves as [)
# If nothing is mentioned, it means all incase of multi-dimensional lists for eg: print(matrix[0]) means every element of first row. Same as matrix[0][:]
lst = [1, 2, 3, 4]
print(lst[ : 2]) # [1, 2]
print(lst[1 : 3]) # [2, 3]
print(lst[-2 : ]) # [3, 4]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0]) # [1, 2, 3]
print(matrix[-2][ : -1]) # [4, 5]
print(matrix[1 : ]) # [[4, 5, 6], [7, 8, 9]]
print(matrix[0][:])


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# List unpacking: assigning the values of the list to variables

#  Without unpacking (Using indexes)
person = ['harry', 30, 'Data Engineer', 'England']
name = person[0]
role = person[2]
print(name) # harry
print(role) # Data Engineer
# This is not a recomemnded method to assign the values of the lists to variables


# Unpacking
name, age, role, country = person
# The order of the variables should be correct
print(name) # harry
print(age) # 30
print(role) # Data Engineer
print(country) # England


# Unpacking using *
# Assign the name and country to the variables but the other values should be assigned to a variable called details
name, *details, country = person
print(name) # harry
print(details) # [30, 'Data Engineer'], here the * converts the remaining data into a list and assigns it to the varable
print(country) # England

# Assign only the name to a variable and others to details
name, *details = person
print(name) # harry
print(details) # [30, 'Data Engineer', 'England']

# Assign only the country to the variable and others to details
*details, country = person
print(details) # ['harry', 30, 'Data Engineer']
print(country) # England

# Assign the role and country to the variables and the rest to details
*details, role, country = person
print(details) # ['harry', 30]
print(role) # Data Engineer
print(country) # England

# Unpacking rules:
# 1. The number of variables must match the values exactly.
# 2. Only one asterisk '*' usage is allowed i.e you cannot use more than one *

list1 = [1, 2, 3, 4, 5]
# This is not valid: value1, value2, value3 = list1, since there are 5 values for 3 variables, so use *
list1 = [1]
value1, *value2 = list1
print(value1) # 1
print(value2) # []
# In the above condition, there is only one value for two variables so first variable gets the value 1
# But the second value is assigned an empty list [] due to the asterisk *


# Underscore (to skip the values)
person = ['harry', 30, 'Data Engineer', 'England']
# In the above list, assign the name and role to the variables and skip the rest
name, _, role, _ = person
print(name) # harry
print(role) # role

# Underscore can also be used in combination with asterisk '*' to skip multiple values
numbers = [1, 2, 3, 4, 5, 6, 7]
# In the above list, assign the vlaues of first and last numbers to the variables and skip the rest
first, *_, last = numbers
print(first) # 1
print(last) # 7


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# Exploring and analyzing lists
numbers = [1, 2, 3, 4, 5]
# Find the max, min, sum and length of the given list.
print('Max: ', max(numbers)) # Max: 5
print('Min: ', min(numbers)) # Min: 1
print('Sum: ', sum(numbers)) # Sum: 15
print('Length: ', len(numbers)) # Length: 5

# all and any
print(all(numbers)) # True
print(all(['a', 'b', 'c'])) # True
print(all([1, 2, 0, 4])) # False
print(all(['a', '', 'c'])) # False

print()

print(any(numbers))
print(any(['a', 'b', 'c'])) # True
print(any([1, 0, 0, 2])) # True
print(any(['a', '', 'c'])) # True
print(any([0, 0, 0])) # False
print(any(['', '', '']))# False

# count and index
print(numbers.count(1)) # 1
print(numbers.count(7)) # 0

# index returns the first position of occurrence. In case of multiple occurrence, it only returns the first occurrence
print(numbers.index(3)) # 2
print(numbers.index(5)) # 4

numbers = [1, 2, 3, 3, 4]
print(numbers.index(3)) # 2

# in
print(2 in numbers) # True
print(5 in numbers) # False

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2) # True


print()
# > and <
# First value of list is compared and if first value of both lists are same then second value is compared
lst1 = [5, 8, 3]
lst2 = [6, 2, 3 ]
print(lst2 > lst1) # True
print(lst1 > lst2) # False

lst1 = [5, 4, 2]
lst2 = [5, 3, 8]
print(lst1 > lst2) # True

print()
# Since is compares the object_id not the value, the object_id is not same for lists having same values but it returns true for copied lists
lst2 = lst1
print(lst2 is lst1) # True
print(lst1 is lst2) # True

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 is lst2) # False


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# List operations: Adding, Removing and Updating
# These operations modify the original list

# Adding new elements to the list using append and insert
# .append()
letters = ['a', 'b', 'c', 'd', 'e']
print(letters) # ['a', 'b', 'c', 'd', 'e']
# Add value 'f' to the above list
letters.append('f')
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f']

# .insert
# add 0 at the beginning
letters.insert(0, 1)
print(letters) # [1, 'a', 'b', 'c', 'd', 'e', 'f']
# add 'A' after a
letters.insert(2, 'A') # [1, 'a', 'A', 'b', 'c', 'd', 'e', 'f']
print(letters)

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
# Add new row at the end of the matrix
matrix.append(['j', 'k', 'l'])
print(matrix) # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

# Add new row at the start of the matrix
matrix.insert(0, ['x', 'y', 'z'])
print(matrix) # [['x', 'y', 'z'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

# In case of matrix, first find the row using the matrix[index] and then perform modifications using same methods as common lists.
# Add 'x' at the end of second row
matrix[1].append('x')
print(matrix) # [['x', 'y', 'z'], ['a', 'b', 'c', 'x'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

# Add 'w' at the start of the first row
matrix[0].insert(0, 'w')
print(matrix) # [['w', 'x', 'y', 'z'], ['a', 'b', 'c', 'x'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]


# Removing elements from the list: clear() and remove()

# clear(): removes all the elements of the list and converts it into a empty list
letters = ['a', 'b', 'c']
# remove all the elements of the list letters
letters.clear()
print(letters) # []

# remove(): removes a specific value from the list i.e delete by value
letters = ['a', 'b', 'a']
# remove 'a' from the list
letters.remove('a')
# Here, remove only removes a single value. If there are multiple values to be removed then multiple remove syntax are needed
print(letters) # ['b', 'a']
letters.remove('a')
print(letters) # ['b']

print()
# pop(): delete by position i.e it deletes value from a specific position in the list
# It deletes the value from the specifc position and returns the deleted value
# If index is not specified then it deletes the last value from the list and returns it
letters = ['a', 'b', 'c']
# Remove the last item from the list
deleted_value = letters.pop(-1)
print(letters)
print(deleted_value)


# Removing rows from the matrix
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
# Remove the first row
matrix.remove(['a', 'b', 'c']) # [['d', 'e', 'f'], ['g', 'h', 'i']]
print(matrix)

# Remove the last row
matrix.pop()
print(matrix) # [['d', 'e', 'f']]

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
# Remove 'e' from the matrix
matrix[1].remove('e')
print(matrix) # [['a', 'b', 'c'], ['d', 'f'], ['g', 'h', 'i']]

# Remove the first item of the last row
matrix[-1].pop(0)
print(matrix) # [['a', 'b', 'c'], ['d', 'f'], ['h', 'i']]

# Remove the last item of the first list
matrix[0].pop()
print(matrix) # [['a', 'b'], ['d', 'f'], ['h', 'i']]


# Update
# Using the index by overwriting the previous value
letters = ['a', 'b', 'c']

# Update the first item to the value 'x'
letters[0] = 'x'
print(letters) # ['x', 'b', 'c']

# Update the second value to 'y'
letters[1] = 'y'
print(letters) # 'x', 'y', 'c']

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
# Update the content of the last list to ['x', 'y', 'z']
matrix[-1] = ['x', 'y', 'z']
print(matrix) # [['a', 'b', 'c'], ['d', 'e', 'f'], ['x', 'y', 'z']]

# Update the first item of the first row to '-'
matrix[0][0] = '-'
print(matrix) # [['-', 'b', 'c'], ['d', 'e', 'f'], ['x', 'y', 'z']]

# Update the second value of the second list to '-'
matrix[1][1] = '-'
print(matrix) # [['-', 'b', 'c'], ['d', '-', 'f'], ['x', 'y', 'z']]


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# Sorting 
# sort() -> Ascending order, modifies the original list
letters = ['c', 'a', 'b']
letters.sort()
print(letters) # ['a', 'b', 'c']

# Sort the given list descending order
letters = ['c', 'a', 'b']
letters.sort(reverse = True)
print(letters) # ['c', 'b', 'a']    

matrix = [
    ['a', 'b', 'c'],
    ['g', 'h', 'i'],
    ['d', 'e', 'f']
]

# Sort the given matrix
matrix.sort()
print(matrix) # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# sort() sorts the matrix on the basis of the first element of each row 
# and if multiple rows have same value then second value of each row is compared and so on

matrix = [
    ['a', 'b', 'c'],
    ['a', 'z', 'i'],
    ['d', 'e', 'f']
]
# sort the second row of the given matrix
matrix[1].sort()
print(matrix) # [['a', 'b', 'c'], ['a', 'i', 'z'], ['d', 'e', 'f']]

# Since sort() modifies the original list, sorted() is used, which doesnot modify the original list.
letters = ['c', 'a', 'b']
# sort the above list without momdifying the original list
new_list = sorted(letters)
print(letters) # ['c', 'a', 'b']
print(new_list) # ['a', 'b', 'c']

# sort in descending order
new_list_desc = sorted(letters, reverse = True)
print(new_list_desc) # ['c', 'b', 'a']

# Reversing a list
letters = ['c', 'a', 'b']
# reverse() is used to reverse a list, and it modifies the original list
letters.reverse()
print(letters) # ['b', 'a', 'c']

numbers1 = [1, 2, 3, 4, 5]
# Reverse the above list without modifying the original list
new_list = reversed(numbers1)
print(new_list) # <list_reverseiterator object at 0x000002BD1B5A6200>
print(numbers1) # [1, 2, 3, 4, 5]
# the type of reversed() is iterator so its output needs to be converetd to list
print(list(reversed(numbers1)))


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# Copying lists
# Using = operator
# = operator is not recommended for copying lists
list1 = [1, 2, 3, 4, 5]
list2 = list1
print('Original: ',list1) # Original:  [1, 2, 3, 4, 5]
print('Copied: ', list2) # Copied:  [1, 2, 3, 4, 5]
# The = operator doesnot copy the values of one list into another
# It simply assigns the same object_id to both the lists. So, if change is made in either of those lists
# then that change is seen in both the list since both list point to the same memory address

# Add 6 to the list2
list2.append(6)
print('Original: ',list1) # Original:  [1, 2, 3, 4, 5, 6]
print('Copied: ', list2) # Copied:  [1, 2, 3, 4, 5, 6]
# Here due to both list pointing to same values, change in one is reflected in another too

# Remove last element from list2
list2.pop()
print('Original: ',list1) # Original:  [1, 2, 3, 4, 5]
print('Copied : ',list2) # Copied :  [1, 2, 3, 4, 5]

# copy() -> shallow copy 
# This copies the top level of the list and creates new values of the object_id which points to different location in the memory
# So, incase of simple lists, it creates new object_id and new values
# Not used for nested lists

letters = ['a', 'b', 'c']
letters_copy = letters.copy()
print('Original: ', letters) # Original:  ['a', 'b', 'c']
print('Copied: ', letters_copy) # Copied:  ['a', 'b', 'c']

# Add 'z' to the copied list
letters_copy.append('z')
print('Original: ', letters) # Original:  ['a', 'b', 'c']
print('Copied: ', letters_copy) # Copied:  ['a', 'b', 'c', 'z']
# Here, the change in the copied list is not reflected in the original list

# problem with copy() in nested lists
matrix = [
    ['a', 'b'],
    ['c', 'd']
]
# list contains object_id which is similar to pointer 
# In case of nested list as above, (object_id of matrix) -> (object_id of list1 and object_id of list2), this is the top level
# object_id of list1 -> values of list1 and object_id of list2 -> values of list2
# copy() only creates object_id in the top level but not in the second layer which points to the same values as the old object_id
# because in the second layer, there is no new object_id
# Practical example is given in the is operator section below

matrix_copy = matrix.copy()
# Remove last row from the original matrix and compare the results with the copied matrix
matrix.pop()
print('Original: ',matrix) # Original:  [['a', 'b']]
print('Copied: ', matrix_copy) # Copied:  [['a', 'b'], ['c', 'd']]
# In the above list, the whole list is removed which is reflected in the top level 
# So, the erasure of whole row in the original list is not reflected in the copied list

matrix = [
    ['a', 'b'],
    ['c', 'd']
]
matrix_copy = matrix.copy()
# Add z at the end of the first row of copied list
matrix_copy[0].append('z')
print('Original: ', matrix) # Original:  [['a', 'b', 'z'], ['c', 'd']]
print('Copied: ', matrix_copy) # Copied:  [['a', 'b', 'z'], ['c', 'd']]
# Since the copy() creates copy of only the top level, change in values of one list is reflected in another list too

# deepcopy(). Import copy module for this
# In case of nested loops, always use deepcopy() since it creates new and independent values and object_id
import copy
matrix = [
    ['a', 'b'],
    ['c', 'd']
]
matrix_copy = copy.deepcopy(matrix)
# matrix_copy = copy.copy(matrix) creates shallow copy of matrix. This method is a general method for creating copy not limited to lists

# Add z at the end of the first row of copied list
matrix_copy[0].append('z')
print('Original: ', matrix) # Original:  [['a', 'b'], ['c', 'd']]
print('Copied: ', matrix_copy) # Copied:  [['a', 'b', 'z'], ['c', 'd']]

#------------------------------------------------------------------------------
# Is operator is used to check if the list are independent or not
# Check the objects_ids of the copied lists using is operator
matrix = [
    ['a', 'b'],
    ['c', 'd']
]
# =
matrix_copy = matrix
print('Same Object_id:', matrix_copy is matrix) # Same Object_id: True

# copy()
matrix_copy = matrix.copy()
print('Same Object_id:', matrix_copy is matrix) # Same Object_id: False
print('Same Object_id for child:', matrix_copy[0] is matrix[0]) # Same Object_id for child: True

# deepcopy()
matrix_copy = copy.deepcopy(matrix)
print('Same Object_id:', matrix_copy is matrix) # Same Object_id: False
print('Same Object_id for child:', matrix_copy[0] is matrix[0]) # Same Object_id for child: False


print('*' * 25)
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
# Combining Lists

# Using '+' operator -> combines the two lists 
letters = ['a', 'b', 'c']
Numbers = [1, 2, 3]

# Combine the above lists
comb = letters + Numbers
print(comb) # ['a', 'b', 'c', 1, 2, 3]

# Using '*' operator
print(letters * 2) # ['a', 'b', 'c', 'a', 'b', 'c']
print(Numbers * 2) # [1, 2, 3, 1, 2, 3]

# Combining using [] and creating nested lists
comb = [letters, Numbers]
print(comb) # [['a', 'b', 'c'], [1, 2, 3]]

# Combining using extend()
# Combine the above lists without creating a new variable for list and extend the pre-existing list letters
letters.extend(Numbers)
print(letters) # ['a', 'b', 'c', 1, 2, 3] 

# Using zip()
# zip() combines each individual elements from both list like one-to-one mapping
# It only processes for elements inside the list that have pair i.e the elements which donot have pairs are ignored
# zip returns an iterator object just like reversed
comb = zip(letters, Numbers)
print(comb) # <zip object at 0x000002EABB34E6C0>
print(list(comb)) # [('a', 1), ('b', 2), ('c', 3)]

# For unequal number of elements in the lists
letters = ['a', 'b', 'c', 'd']
Numbers = [1, 2, 3]
comb = zip(letters, Numbers)
print(list(comb)) # [('a', 1), ('b', 2), ('c', 3)], here the value which doesnot have a pair for matching is ignored

# zip can also be paired wih string values zip(list1, list2, string)
letters = ['a', 'b', 'c']
Numbers = [1, 2, 3]
comb = zip(letters, Numbers, 'Hi')
print(list(comb)) # [('a', 1, 'H'), ('b', 2, 'i')], here 'c' and 3 cannot form a pair with Hi so both of them are ignored


