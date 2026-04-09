# Abstraction
# The process of hiding complex implementation details and showing only the essential features of an object

# The attributes and methods are hidden
# You can simply access methods and attributes by creating objects
# So by creating objects, we can simply access the methods and attributes without understanding the complex working of the code inside a class



# For example in many real case scenario, the security code inside the main class in not written and the security method is made abstract

from abc import ABC, abstractmethod # ABC -> Abstract Base Class
# An abstract class is a class that contains atleast one abstract method and any number of non-abstract class
# An abstract class must inherit from ABC
# An abstract method is a method that is essentialy empty an doesnot have any code inside it



# Abstraction is also used to define constraints

# The constraint for the given code is:
# Without creating security method, child class cannot access the methods of the parent class
# Without creating security, the WebApp cannnot connect to the database method of BankApp

class BankApp(ABC):

    def database(self):
        print('connected to database')

    @abstractmethod
    def security(self):
        pass

class WebApp(BankApp):

    def mobile_login(self):
        print('Login to mobile')

    def security(self):
        print('Mobile Security')


# WebApp inherits from abstract class which is BankApp
# The object of the WebApp cannot be created unless a method having same name as abstract method is created and code is written inside it
obj = WebApp()
obj.database() # connected to database
obj.mobile_login() # Login to mobile


# If an abstract class has multiple abstract methods then same number of methods have to be created inside another class to create objects
class BankApp(ABC):

    def database(self):
        print('connected to database')

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass

class WebApp(BankApp):

    def mobile_login(self):
        print('Login to mobile')

    def security(self):
        print('Mobile Security')

    def display(self):
        print('Mobile display')


# If object is created without making required number of methods same as abstract methods then it throws error
# If security is created inside the child class but display is not created then it throws the error below:
# TypeError: Can't instantiate abstract class WebApp without an implementation for abstract method 'display'
obj = WebApp()
obj.database() # connected to database
obj.display() # Mobile display
obj.security() # Mobile Security
obj.mobile_login() # Login to mobile
