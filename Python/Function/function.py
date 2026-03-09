# Generic function
# Write a function that prints python
def text():
    print('python')

text() # python


# Parametrized function
# Write a function that cleans the name 
def clean_name(name):
    print(name.strip().lower())

clean_name(' pythoN ') # python
clean_name('   AlEx ') # alex


# Global and Local variable
# Global variable can be accessed from anywhere
# Local variable can be accessed inside the function only and its value is destroyed after the execution of the function
case_rule = 'lower'
def clean_name1(name):
    cleaned = name.strip() # Local variable
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    print(f'Raw Data: {name}') # Raw Data::   pyTHon
    print(f'Cleaned Data: {cleaned}') # Cleaned Data: python

clean_name1('  pyTHon  ')
    

print()
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# There are two ways of passing values to the function:
# One is positional arguments i.e based on the order of parameters defined
# Other is the keyword argument i.e based on the name of parameters defined
 
def clean_fullname(firstname, lastname, country = 'n/a'):
    first = firstname.strip().lower()
    last = lastname.strip().lower()
    full_name = first + ' ' + last
    print(f'{full_name} is from {country}')

# Positional arguments -> order matters
clean_fullname('  will ', 'SmItH ', 'USA') # will smith is from USA

# If order is wrong then the output will also be wrong
clean_fullname('USA ', '  will ', 'smITH') # usa will is from smITH

# Keyword Arguments -> order doesnot matter
clean_fullname(country = 'USA ', firstname = '  will ', lastname = 'smiTH') # will smith is from USA

# If there are several parameters in a function then keyword arguments is recommended otherwise use positional arguments.

# Mix arguments -> Not recommended
# Rules:
# 1. Always start with positional one
# 2. Positional argument cannot start after keyword argument
clean_fullname(' wiLl  ', lastname = ' smiTh', country = 'USA ') # will smith is from USA

# Rule 1
# clean_fullname(firstname = ' will ', ' smiTH', country = 'USA ') # SyntaxError: positional argument follows keyword argument

# Rule 2
# clean_fullname('  wilL ', lastname = ' smiTH ', 'USA ') # SyntaxError: positional argument follows keyword argument

# Default parameter
# Rules: 
# 1. First all the parameter without the default must be defined before using default value
# 2. Default parameter cannot be used before non-default parameters
# for eg:
# rule 1: def clean_fullname(firstname = 'will', lastname, country): # Not valid
# rule2: def clean_fullname(firstname, lastname = 'smith', country): # Not valid

clean_fullname('  will ', ' smiTH') # will smith is from n/a
clean_fullname(firstname = ' wiLL', lastname = 'smiTH  ') # will smith is from n/a


print()
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# *args and **kwargs
# args and kwargs are used when the number of parameter needed in a function is not known
# *args -> positional arguments
# **kwargs -> keyword arguments

# *args
def total(*args):
    print(type(args)) # <class 'tuple'>
    print(sum(args))

total(2, 3) # 5
total(2, 3, 4) # 9
total(2, 3, 4, 5, 5.1) # 19.1
# args is used for functions having similar kind of values such as a sequence of numberes or strings 
total(5.5, 5, 5, 5.5) # 21.0

# **kwargs
def create_user(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    print(kwargs)

# It accepts only the keyword arguments i.e name of variable has to be specified
create_user(first_name = 'Jason',
            last_name = 'Jackson',
            age = 25,
            country = 'Germany')
# output: {'first_name': 'Jason', 'last_name': 'Jackson', 'age': 25, 'country': 'Germany'}
# Since key value pair is passed as arguments, the data type of kwargs is dict

# The number of parameters can be changed everytime
create_user(first_name = 'Javier',
            last_name = 'Penia',
            age = 28,
            country = 'Mexico')
# {'first_name': 'Javier', 'last_name': 'Penia', 'age': 28, 'country': 'Mexico'}

#    args                      |   kwargs
#--------------------------------------------------------------------------------|
# 1. data type -> tuple        |   data type -> dict
# 2. same type of information  |   different type of information, same as in dict i.e names and values


print()
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# Return type function
def Clean_name(name):
    cleaned = name.strip().lower()
    return cleaned

cleaned_name = Clean_name('   AleX')
print(cleaned_name) # alex

cleaned_name = Clean_name('')
print(cleaned_name) # 
# If empty string is passed as in input then empty string is returned as output
# So to solve this problem function is modified to return None if input string is empty

def Clean_name(name):
    if name == '':
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned
    
cleaned_name = Clean_name('')
print(cleaned_name) # None
print(Clean_name('  AlEx')) # alex

# Returning multiple values
def clean_name(name):
    up_name = name.strip().upper()
    lo_name = name.strip().lower()
    return up_name, lo_name
names = clean_name('  ElLEn')
print(names, type(names)) # ('ELLEN', 'ellen') <class 'tuple'>
# If multiple return values are stored in a same variable then it is stored as tuple.

# Multiple variables can be defined in a sequence to store multiple return values
upper_name, lower_name = clean_name('  ElLEn')
print(upper_name, lower_name) # ELLEN ellen
