# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

class Point:
    
    def __init__(self, a, b):
        self.x = a
        self.y = b
    

    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    

    def eucledian_distatnce(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
    

    def distance_from_origin(self):
        return self.eucledian_distatnce(Point(0, 0)) # We can also create object of a class inside that class
        # return ((self.x)**2 + (self.y)**2)**0.5

    
class Line:
    # Ax + By + C = 0

    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)

    def check_line_point(line, point): # self = line, other = point
        if line.A * point.x + line.B * point.y + line.C == 0:
            print('The point lies on the line')
        else:
            print('The point doesnot lie on the line')


    def line_and_point_shortest_distance(line, point):
        return (abs(line.A * point.x + line.B * point.y + line.C) / (line.A**2 + line.B**2)**0.5)
    



x1 = Point(1, 0)
print(x1) # (0,0)
x2 = Point(4, 0)
print(x2) # (4,1)
print(x1.eucledian_distatnce(x2)) # 3.0
print(x2.distance_from_origin()) # 4.0

l1 = Line(1, 1, 1)
print(l1) # 1x + 1y + 1 = 0
l1.check_line_point(Point(1, -2)) # The point lies on the line
l1.check_line_point(x2) # The point doesnot lie on the line

x3 = Point(1, -2)
print(l1.line_and_point_shortest_distance(x3)) # 0.0, since the point lies on the line
print(l1.line_and_point_shortest_distance(x1)) # 1.414213562373095

#--------------------------------------------------------------------------------------------------------------------------------------------
# Attribute creation from outside of the class
class Person:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greeting(self):
        if self.country == 'Nepal':
            print('Namaste')
        else:
            print('Hi')

p = Person('Hari', 'Nepal')
p.greeting() # Namaste
print(p.name) # Hari

# Let's access a attribute tha doesnot exist
# print(p.age) # AttributeError: 'Person' object has no attribute 'age'
# So we can create object attributes from outside the class
p.age = 25
print(p.age) # 25

# This newly created attribute only exists for that object and it cannot be accessed by other objects
q = Person('Anish', 'Bhutan')
# print(q.age) # AttributeError: 'Person' object has no attribute 'age'

#--------------------------------------------------------------------------------------------------------------------------------------------
# Reference Variables
# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to an existing object does not create a new object
# when p = Person('hari', 'Nepal'), p is the reference variable that holds the address of the created object. So, p is not an object
# Person('hari', 'Nepal') is object

class Person:

    def __init__(self):
        self.name = 'Anish'
        self.country = 'Nepal'

# Object can be created without reference variable
print(Person()) # <__main__.Person object at 0x000002AF314280E0>

# Object creation using reference variable
p = Person()
q = p
# Here p contains address of object which is passed to the variable q so both variable point to the same address in the memory which is the object
print(id(p)) # 2363153613264
print(id(q)) # 2363153613264

# So if one reference variable is used to change the attribute of the object then it is reflected in another variable too
print(p.name) # Anish
print(q.name) # Anish
q.name = 'Ayush'
print(p.name) # Ayush
print(q.name) # Ayush

#--------------------------------------------------------------------------------------------------------------------------------------------
# Pass by reference
# Python allows you to pass object as argument to the function outside the class, and function can also return object outside the class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Outside the class
def pass_and_return_object(person):
    print(f'Hi, My name is {person.name} and I am {person.age} years old')
    p1 = Person('Harry', 25)
    return p1

p = Person('Brook', 30)
# To access the function outside object cannot be used
q = pass_and_return_object(p) # Hi, My name is Brook and I am 30 years old
print(q.name) # Harry
print(q.age) # 25



class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# OUtside the class
def greet(person):
    print(id(person)) # 2125688280592, so when an object is passed to a function, the address of that object is passed instead of the object itself
    person.name = 'Harry'
    print(person.name) # Harry


p = Person('Robin', 20)
print(id(p)) # 2125688280592
greet(p)
print(p.name) # Harry


#--------------------------------------------------------------------------------------------------------------------------------------------
# Mutability of object
# Objects are mutable


class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  person.name = 'ankit'
  return person

p = Person('nitish','male')
print(id(p)) # 2657717590912
p1 = greet(p)
print(id(p1)) # 2657717590912

#--------------------------------------------------------------------------------------------------------------------------------------------
# Encapsulation
# It means hiding the data that are sensitive

class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

p1 = Person('nitish','india')
p2 = Person('steve','australia')
print(p1.name)
print(p2.name)
# The name and country(attributes) are called instance variables since they are different for each objects


# Using private access specifier
# The best practice is to make the attributes private and using getter and setters to access and modify these values
# Any attribute can be made private by using __ before the attribute name
# Inside the variable, the private attribute is accessed using __variable 
# When a private variable is created, the name of the variable changes to _ClassName__variable, same for methods too
# SO by using __variable, the original attribute cannot be accessed
# To access the private variable from outside the class, one must use the name _ClassName__variable
# In python, no variable is truly private, mentioning a __before any attribute is a indication that the attribue is private.



class Atm:

    # Constructor
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        # print(id(self)) # 2156543506048
        #self.menu()

    # After making attributes, make getters and setters for each attributes to access and modify the private attributes
    # Getter
    def get_balance(self):
        return self.__balance
    
    # Setter
    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('Error occured')
    
    def __menu(self):
        user_input = input("""
Welcome to the Atm application.
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Anything else to exit                                                   
""")

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    

    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.__pin = user_pin

        user_balance = int(input('Enter your balance: '))
        self.__balance = user_balance

        print('Pin created successfully')

        self.__menu()


    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.__pin:
            new_pin = input('Enter your new pin: ')
            self.__pin = new_pin
            print('Pin updated successfully')
        else:
            print('Pin didnot match')

        self.__menu()


    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.__pin:
            print('Your blanace is', self.__balance)
        else:
            print('Pin didnot match')

        self.__menu()


    def withdraw(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.__pin:
            amount = int(input('Enter amount to withdraw: '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('Balance withdraw successfull')
                print('Remaining balance is', self.__balance)
            else:
                print('Balance not sufficient')
        else:
            print('Pin didnot match')

        self.__menu()


obj1 = Atm()
# print(obj1.__balance) # AttributeError: 'Atm' object has no attribute '__balance'
print(obj1._Atm__balance) # 0
# obj1.__menu() # AttributeError: 'Atm' object has no attribute '__menu'

# Usually the attributes are made private but methods are not made private so above code is just an example
# obj1._Atm__menu()
# Using _ClassName__variable for accessing private attributes is not a good practice, so use getters and setters

obj1.set_balance(5000)
print(obj1.get_balance()) # 5000

# Now if a new attribute is added with the same name __variable then it will be treated as different variable than the private one
obj1.__balance = 25
print(obj1.__balance) # 25
print(obj1._Atm__balance) # 5000

# -----------------------------------------------------------------------------------------------------------------------------------------
# Collection of objects

# List of objects
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Harry', 25)
p2 = Person('Scott', 30)
p3 = Person('Ryan', 35)
lst = [p1, p2, p3]
for i in lst:
    print(i.name, i.age)
# Harry 25
# Scott 30
# Ryan 35

# Dictionary of objects
dict1 = {
    'object1': p1,
    'object2': p2,
    'object3': p3
}
for i in dict1:
    print(dict1[i].name)
# Harry
# Scott
# Ryan

# ---------------------------------------------------------------------------------------------------------
# Static variables
# Points to remember about static
# Static attributes are created at class level.
# Static attributes are accessed using ClassName.
# Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined.
# The value stored in static attribute is shared between all instances(objects) of the class in which the static attribute is defined.

# In the above atm code, add a feature which keeps a track of number of users
class Atm:

    __user_number = 0
    # Constructor
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
         # Since static variable doesn't belong to any object, so self cannot be used to access these variables
        Atm.__user_number += 1
        #self.menu()

    # Since this function returns static variable so self cannot be used in this function
    @staticmethod
    def get_user_number():
        return Atm.__user_number

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('Error occured')
    
    def menu(self):
        user_input = input("""
Welcome to the Atm application.
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Anything else to exit                                                   
""")

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    

    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.__pin = user_pin

        user_balance = int(input('Enter your balance: '))
        self.__balance = user_balance

        print('Pin created successfully')

        self.menu()


    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.__pin:
            new_pin = input('Enter your new pin: ')
            self.__pin = new_pin
            print('Pin updated successfully')
        else:
            print('Pin didnot match')

        self.menu()


    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.__pin:
            print('Your blanace is', self.__balance)
        else:
            print('Pin didnot match')

        self.menu()


    def withdraw(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.__pin:
            amount = int(input('Enter amount to withdraw: '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('Balance withdraw successfull')
                print('Remaining balance is', self.__balance)
            else:
                print('Balance not sufficient')
        else:
            print('Pin didnot match')

        self.menu()

p1 = Atm()
# p1.get_user_number() # TypeError: Atm.get_user_number() takes 0 positional arguments but 1 was given
# Since static variables belong to the class and not to the object so p1 cannot access the user_number
print('Number of users:',Atm.get_user_number()) # 1
p2 = Atm()
print('Number of users:',Atm.get_user_number()) # 2
p3 = Atm()
print('Number of users:',Atm.get_user_number()) # 3


# Static Method
class Lion:
  __water_source = "well in the circus"

  def __init__(self, name, gender):
      self.__name = name
      self.__gender = gender

  def drinks_water(self):
      print(self.__name,"drinks water from the",Lion.__water_source)
      
  @staticmethod
  def get_water_source():
      return Lion.__water_source

simba = Lion("Simba","Male")
simba.drinks_water()
print( "Water source of lions:",Lion.get_water_source())

