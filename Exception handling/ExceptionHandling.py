# There are 2 stages where error may happen in a program
# During compilation -> Syntax Error
# During execution -> Exceptions -> Run time error

# Syntax Error
# Something in the program is not written according to the program grammar.
# Error is raised by the interpreter/compiler
# You can solve it by rectifying the program

# There are various types of errors:
# 1. SyntaxError
# 2. IndentationError
# 3. IndexError
# 4. ModuleNotFoundError
# 5. KeyError
# 6. TypeError
# 7. ValueError
# 8. NameError
# 9. AttributeError 


# Exceptions
# If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.

# Exceptions are raised by python runtime
# You have to takle is on the fly
# Examples
# Memory overflow
# Divide by 0 -> logical error
# Database error

# try except block -> try catch



from sys import exception


with open('sample.txt', 'w') as f:
    f.write('Hello World')


try:
    with open('ample.txt', 'r') as f:
        print(f.read())
except:
    print('File not Found') # If file is not found, it will display this message but the execution of code is not disturbed
# behaves as if-else

print()

# Handling exceptions using exception class
try:
    with open('sample.txt', 'r') as f:
        print(f.read())
        print(5/0)
except Exception as e:
    print(e) # division by zero
    # By doing so, it automatically handles the specific exception as per default procedure


print()


# Catching specific expections
try:
    b = 5
    with open('sample.txt', 'r') as f:
        print(f.read())
        print(b)
        l = [1, 2, 3]
        print(5/5)
        print(l[20])
except FileNotFoundError:
    print('File Not Found')
except NameError:
    print('Name is Wrong')
except ZeroDivisionError:
    print('Denominator cannot be zero')
except Exception as e: # This catches other exceptions not defined above
    print(e)


print()


# try else
# The code that might generate exception is kept inside the try block and except handles those exceptions
# The code that should be executed if no exception occurs is kept inside the else block
try:
    f = open('sample.txt', 'r')
except FileNotFoundError:
    print('File not found')
except Exception:
    print('Something is wrong')
else:
    print(f.read())
    f.close()


print()


# Finally
# The code inside finally is always executed regardless of whether the execution occurs or not
try:
    f = open('ample.txt', 'r')
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('This is always executed')
# File not found
# This is always executed

print()


# Raising exceptions
# a = 5
# if type(a) == int:
#     raise Exception('Integer is not supported')


class Bank:

    def __init__(self, balance):
        self.balance  = balance

    def withdraw(self, amount):
        if amount < 0:
            raise Exception('Amount cannot be negative')
        elif self.balance < amount:
            raise Exception('Balance is not sufficient')
        else:
            self.balance = self.balance - amount
        

obj = Bank(5000)

try:
    obj.withdraw(10000)
except Exception as e:
    print(e)
else:
    print(obj.balance) # Balance is not sufficient


print()


# Creating custom exception class
# When exceptions out of the exception hierarchy occurs then custom exceptions can be created
# The custom exception class must inherit from Exception class
# In the above code, inplace of Exception, MyException is written to call the custom exception class
class MyException(Exception):

    def __init__(self, message):
        print(message) # When object of this class is created, this constructor is executed


class Bank:

    def __init__(self, balance):
        self.balance  = balance

    def withdraw(self, amount):
        if amount < 0:
            raise MyException('Amount cannot be negative')
        elif self.balance < amount:
            raise MyException('Balance is not sufficient')
        else:
            self.balance = self.balance - amount


obj = Bank(5000)
try:
    obj.withdraw(-5000) # Amount cannot be negative
except MyException:
    pass # pass is used since the message to be displayed is already written inside the constructor of the custom exception class
else:
    print(obj.balance)
