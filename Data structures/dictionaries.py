# dictionary -> key-value pair
# Ordered
# Duplicates: for values only. Duplicate of keys is not allowed
# Not indexed but keyed
# Mutable

my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a': 40
}

# ordered and duplicates of values allowed but not of keys
print(my_dict) # {'a': 40, 'b': 20, 'c': 30}
# In case of duplicate values, only recent value is stored and showed whereas the old value is ignored

# Not indexed but keyed
print(my_dict['b']) # 20

# Mutable
my_dict['c'] = 50
print(my_dict) # {'a': 40, 'b': 20, 'c': 50}

# Accessing dictionary
user = {
    'id': 1,
    'age': 23,
    'city': 'London'
}
print(user['city']) # London
# If the key is not present in the dict then it throws error and breaks the execution of the code
# print(user['name']) # KeyError: 'name'

# So to solve this problem, get method is used
# It returns None by default if no key found
# The return parameter can also be defined by the user
print(user.get('Name')) # None

# Print default if key is not found
print(user.get('name', 'Not Found')) # Not Found

# Using in operator
print('age' in user) # True
print('name' in user) # False

# View Object
# Returns all the keys of a dict and values
print(user.keys()) # dict_keys(['id', 'age', 'city'])
print(user.values()) # dict_values([1, 23, 'London'])
print(user.items()) # dict_items([('id', 1), ('age', 23), ('city', 'London')])
# user.items() is used for looping through the dictionary as it returns key-value pairs in a tuple format

# Looping
for u in user:
    print(u, user[u])
# id 1
# age 23
# city London

# As we can see, the below method is easier to understand so, to loop through a dictionary, .items() is used
for key, value in user.items():
    print(key, value)
# id 1
# age 23
# city London

# Add, Remove and Update
# Add
user['name'] = 'Alex'
print(user) # {'id': 1, 'age': 23, 'city': 'London', 'name': 'Alex'}

# Update
user['age'] = 25
print(user) # {'id': 1, 'age': 25, 'city': 'London', 'name': 'Alex'}

# Update using .update()
# .update adds new keys and updates existing ones using another dictionary inside the .update()
user.update({'age': 55, 'city': 'New York', 'Surname': 'Smith'})
print(user) # {'id': 1, 'age': 55, 'city': 'New York', 'name': 'Alex', 'Surname': 'Smith'}

# Pop using keys
# pop() empty cannot be used, key must be entered inside the pop
deleted = user.pop('Surname')
print('Deleted Value:', deleted) # Deleted Value: Smith
print(user) # {'id': 1, 'age': 55, 'city': 'New York', 'name': 'Alex'}

# If non existing key is used inside the pop then it throws error and breaks the execution of whole code
# deleted = user.pop('Job') # KeyError: 'Job'
# So to solve this problem, you can define defalut value inside the pop 
deleted = user.pop('Job', 'Not Found')
print('Deleted Value:', deleted) # Deleted Value: Not Found

# popitem() -> Removes the last key-value pair
deleted = user.popitem()
print(deleted) # ('name', 'Alex')
print(user) # {'id': 1, 'age': 55, 'city': 'New York'}


# Creating dictionary with same values or if the values are not known
user = {
    'id': None,
    'name': None,
    'age': None,
    'city': None
}
# This can also be done using dict.fromkeys() where same value can be assigned to all the keys
user = dict.fromkeys(['id', 'name', 'age', 'city'], None)
print(user) # {'id': None, 'name': None, 'age': None, 'city': None}

user = dict.fromkeys(['id', 'name', 'age', 'city'], 'Not Defined')
print(user) # {'id': 'Not Defined', 'name': 'Not Defined', 'age': 'Not Defined', 'city': 'Not Defined'}

# Create new dict
# Keep only keys with string values
# Convert values to uppercase
user = {
    'id': 1,
    'name': 'alex',
    'age': 30,
    'city': 'vegas'
}

# Using dict comprehension
new_dict = {
    key: value.upper()
    for key, value in user.items()
    if isinstance(value, str)
}
print(new_dict) # {'name': 'ALEX', 'city': 'VEGAS'}
