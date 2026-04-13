# Namespaces
# A namespace is a space that holds names(identifiers). 
# Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values) i.e both variables and functions

# There are 4 types of namespaces:

# Builtin Namespace
# Global Namespace
# Enclosing Namespace
# Local Namespace


# Example 1

def my_function(a, b):
    result = a + b
    # View the local namespace as a dictionary
    print(locals()) 

my_function(10, 5)
# Output: {'a': 10, 'b': 5, 'result': 15}
# Here, the output is the local namespace that is a dictionary


# Scope and LEGB Rule
# A scope is a textual region of a Python program where a namespace is directly accessible.
# The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope.
#  If the interpreter doesn’t find the name in any of these locations, then Python raises a NameError exception.


# local and global
# global var
a = 2

def temp():
  # local var
  b = 3
  print(b)

temp()
print(a)



# local and global -> same name
a = 2

def temp():
  # local var
  a = 3
  print(a) # 3

temp()
print(a) # 2
# LEGB rule, local variable has the highest priority



# local and global -> local can access the global variable even though that variable is not in local scope
z = 2

def temp():
  # local var
  print(z) # 2

temp()
print(z) # 2



# local and global -> editing global
a = 2

def temp():
  # local var
  a += 1
  print(a)

temp()
print(a) # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
# In python, global variable cannot be directly edited from the local scope



a = 2

def temp():
  # local var
  global a
  a += 1
  print(a) # 3

temp()
print(a) # 3
# To change the global variable from the local scope, write global variable_name inside the global scope(function) 



# local and global -> global created inside local
def temp():
  # local var
  global a
  a = 1
  print(a) # 1

temp()
print(a) # 1
# Variable created insdie local scope using global keyword behave as global variable
# Such variables once created, can be accessed from anywhere same as global variable



# Built-In scope
# All the elements that can be directly used without importing from anywhere
import builtins
print(dir(builtins)) # eg :['list', 'map', 'tuple', 'ArithmeticError', 'print'.........]


# Enclosing Scope
# This is seen in nested functions
# The scope of outer function is called enclosing or non-local scope
a = 1

def outer():
  def inner():
    print(a)
  inner()
  print('Outer Function') # Here, outer() behaves as enclosing scope for inner(), and the scope of inner() is local

outer()
print('Main Program')
# 1
# Outer Function
# Main Program


# To change the value of vaiable in enclosing scope, nonlocal keyword is used same as global keyword
# Here, the inner function can access the enclosing variable i.e outer vaiable but the inner function cannot directly change it
# So nonlocal keyword is used

def outer():
  a = 5
  def inner():
    nonlocal a
    a += 1
    print('Inner function a =', a)
  inner()
  print('Outer Function a=', a)

outer()
print('Main Program')
# Inner function a = 6
# Outer Function a= 6
# Main Program

#----------------------------------------------------------------------------------------------------------
# Decorators
# A decorator in python is a function that receives another function as input and adds some functionality(decoration) to it
# and returns it.
# This can happen only because python functions are 1st class citizens.
# There are 2 types of decorators available in python
# Built in decorators like @staticmethod, @classmethod, @abstractmethod and @property etc
# User defined decorators that we programmers can create according to our needs

# Functions are called first-class citizens (or first-class objects) in Python 
# because they are treated like any other object, such as integers or strings.
# This means they can be manipulated and passed around throughout a program without restrictions.

# Functions are first class citizens?

def modify(func, num):
  return func(num)

def square(value):
  print(value**2)

modify(square, 2) # 4
# Here functions can be passed and returned aa other objects such as: integers or strings


# Simple example of decorator without using an actual decorator
def decorator(func):
  def wrapper():
    print('-' * 10)
    func()
    print('-' * 10)
  return wrapper 

def display():
  print('Hello world')

def happy():
  print('Happy Birthday')

a = decorator(display)
a() # This has to be done because decorator returns wrapper but not wrapper(). If there was wrapper() inside the decorator 
# in the return statement then this step need not to be written
# ----------
# Hello world
# ----------

b = decorator(happy)
b()
# ----------
# Happy Birthday
# ----------


# By using decorator, the above step of returing and then again calling that returned function need not to be written

def decorator_function(func):
  def wrapper():
    print('=' * 15)
    func()
    print('=' * 15)
  return wrapper
  
# Here, a decorator is written above another function which is passed as input to the decorator
# By doing so, the decorator function is called automatically when the input function is called
@decorator_function
def display():
  print('Hello World')

@decorator_function
def happy():
  print('Happy Birthday')


display()
# ===============
# Hello World
# ===============

happy()
# ===============
# Happy Birthday
# ===============


# Decorator to find the execution time
import time
def timer(func):
  def wrapper():
    start = time.time()
    func()
    print(f'Time taken by {func.__name__} is {start - time.time()} seconds') # Function name is accessed using function_name.__name__
  return wrapper

@timer
def display():
  print('Hello World')
  time.sleep(2)

display()
# Hello World
# Time taken by display is -2.0003774166107178 seconds


# For the same code above, use parametrized functions
# In case of parametrized input function, pass the normal func name inside the decorator
# Pass the *args inside the wrapper function to handle any number of arguments
# Inside the wrapper function, when calling the input function, pass *args inside the function call

import time
def timer(func):
  def wrapper(*args):
    start = time.time()
    func(*args)
    print(f'Time taken by {func.__name__} is {start - time.time()} seconds') 
  return wrapper

@timer
def display():
  print('Hello World')
  time.sleep(2)

@timer
def square(value):
  print(value**2)
  time.sleep(3)

@timer
def power(num, pow):
  print(num**pow)
  time.sleep(2)

display()
# Hello World
# Time taken by display is -2.0015764236450195 seconds

square(5)
# 25
# Time taken by square is -3.0018491744995117 seconds

power(2, 3)
# 8
# Time taken by power is -2.0007576942443848 seconds


# Decorator with arguments
# Make a decorator that check the data type and if wrong data type is given then throw error
# Here the decorator function takes data type as input, then function is given as input to the next function
# then another function takes *args as arguments. So in total, three functions are required
def check(data_type):
  def outer_wrapper(func):
    def inner_wrapper(*args):
      if type(*args) == data_type: # Here, args is a tuple but *args is an integer because it is an unpacked value
        func(*args)
      else:
        raise TypeError('Wrong Datatype')
    return inner_wrapper
  return outer_wrapper

@check(int)
def square(value):
  print(value**2)

square(2) # 4
# square('two') # TypeError: Wrong Datatype
# The above code only works for a single argument function


# In case of multiple aguments input funtion
def check(data_type):
  def outer_wrapper(func):
    def inner_wrapper(*args):
      if all(type(arg) == data_type for arg in args): # all returns true if all the values are true
        func(*args)
      else:
        raise TypeError('Wrong Datatype')
    return inner_wrapper
  return outer_wrapper

@check(int)
def power(value, power):
  print(value**power)


power(5, 2) # 25
# power('hddsjhsjf') # TypeError: Wrong Datatype


