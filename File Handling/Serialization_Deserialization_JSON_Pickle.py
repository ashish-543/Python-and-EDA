# In text file, data of any data type is converted to string so we loose the original data type of the data.
# So to solve this problem, we use JSON data format

# Serialization: Process of converting python data types to JSON format
# Deserialization: Process of converting JSON to python data types
# JSON is a universal data format that almost every programming language understands
# First json module have to be imported


# list
import json
# Serialization
lst = [1, 2, 3, 4, 5]
with open('serial.json', 'w') as f:
    json.dump(lst, f) # Same as f.write(). json.dump(data, file_handler_object)

# Deserialization
with open('serial.json', 'r') as f:
    data = json.load(f)
    print(type(data)) # list


# dict
# Serialization
dict = {
    'name': 'Harry',
    'age': 30,
    'country': 'Japan',
    'role': 'data engineer'
}
with open('serial.json', 'w') as f:
    # json.dump(dict, f) # Indentation can also be added which adds indent to the data inside dictionary
    # Output inside file: {"name": "Harry", "age": 30, "country": "Japan", "role": "data engineer"}
    json.dump(dict, f, indent = 4)
    # {
        # "name": "Harry",
        # "age": 30,
        # "country": "Japan",
        # "role": "data engineer"
    # }

# Deserialization
with open('serial.json', 'r') as f:
    data = json.load(f)
    print(data) # {'name': 'Harry', 'age': 30, 'country': 'Japan', 'role': 'data engineer'}
    print(type(data)) # <class 'dict'>


# tuple
# When tuple is stored in the file using json, it is stored as list.
# tuple looses its data type and gets converted to list
# Serialization
tup = (1, 2, 3, 4)
with open('serial.json', 'w') as f:
    json.dump(tup, f) # output in file: [1, 2, 3, 4]

# Deserialization
with open('serial.json', 'r') as f:
    data = json.load(f)
    print(data) # [1, 2, 3, 4]
    print(type(data)) # <class 'list'>
    # As we can see, tuple is converted to list
    

# ----------------------------------------------------------------------------------------------------------------------
# Serializing and deserializing objects
# Using normal json format, the objects cannot be serialized as it is
# Which means that once the objects are serialized, they loose the functionality of oop
# So the deserialized objects cannot use the functionality of the classes and behave as normal data types

# First let's see what the problem is with normal json format

class Person:

    # Constructor
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

# format to be printed
# -> Harry Watson age -> 25 gender -> male

person = Person('Harry', 'Watson', 25, 'male')

# Define a function that specifies the format in which the object will be serialized
def show_object(person):
    if isinstance(person, Person):
        return f'-> {person.fname} {person.lname} age -> {person.age} gender -> {person.gender}'
    
# The object can be stored in any format
# In dict format
def show_object_dict(person):
    if isinstance(person, Person):
        return {
            'Firstname': person.fname,
            'Lastname': person.lname,
            'Age': person.age,
            'Gender': person.gender
        }

with open('file.txt', 'w') as f:
    json.dump(person, f) # TypeError: Object of type Person is not JSON serializable
    # Here object directly cannot be serialized so we have to specify how it will be serialized
    # i.e we have to specify how the object will be stored or displayed inside the file by specifying a method
    # So we have to pass the method inside the json.dump
    json.dump(person, f, default = show_object)
# # Output inside the file
# # "-> Harry Watson age -> 25 gender -> male"

with open('file.txt', 'w') as f:
    json.dump(person, f, default = show_object_dict, indent = 4)
# # output inside file
# {
#     "Firstname": "Harry",
#     "Lastname": "Watson",
#     "Age": 25,
#     "Gender": "male"
# }

# Deserializing
with open('file.txt', 'r') as f:
    data = json.load(f)
    print(type(data)) # <class 'dict'>
    # Here the object looses its functionality and is now dictionary data type

# So to solve this problem, picking is used
# Pickling serializes data as it is and the object doesnot loose its oop functionality
# Pickling is a process whereby a python object hierarchy is converted into a byte stream, and unpickling is the inverse operation
# whereby a byte stream(from binary files or bytes-like object) is converted back into object hierarchy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f'Hi my name is {self.name} and I am {self.age} years old')

p = Person('Aiden', 30)

# pickle dump
import pickle
with open('person.pkl', 'w') as f:
    pickle.dump(p, f) # TypeError: write() argument must be str, not bytes
    # So binary mode must be used while working with pickle files

with open('person.pkl', 'wb') as f:
    pickle.dump(p, f)

# pickle load
with open('person.pkl', 'rb') as f:
    data = pickle.load(f)
    print(type(data)) # <class '__main__.Person'>

# This object(data) can access the methods of the class Person
data.display_info() # Hi my name is Aiden and I am 30 years old



# pickle VS JSON
# pickle lets the user store data in binary format without loosing the oop functionality
# JSON lets the user store data in human-readable format
