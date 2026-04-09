# Class Relationships
# 1. Aggregation 
# 2. Inheritance


# Aggregation (Has-A Relationship)
# In this relationship, one class owns another class

# Customer-----<Has-A>-----Address
# This relationship is used when a class owns another class and it reduces redundant code and increases code reusability
class Customer:

    def __init__(self, name, age, address):
        self.Name = name
        self.Age = age
        self.Address = address

    def print_address(self):
        # Here the address in the constructor behaves as an object since object was passed as argument
        # Here the Address below is not the name of class but the name of attribute defined above
        print(self.Address.continent, self.Address.country, self.Address.get_city())
        # Since city is a private attribute attribute, above code can also be written as:
        # print(self.Address.continent, self.Address.country, self.Address._Address__city)
        # Here, self.Address.continent -> Customer.Address.continent

    def edit_profile(self, new_name, new_age, new_continent, new_country, new_city):
        self.Name = new_name
        self.Age = new_age
        self.Address.edit_address(new_continent, new_country, new_city)


class Address:

    def __init__(self, continent, country, city):
        self.continent = continent
        self.country = country
        self.__city = city
    
    # Getter
    def get_city(self):
        return self.__city
    
    def edit_address(self, new_continent, new_country, new_city):
        self.continent = new_continent
        self.country = new_country
        self.__city = new_city

add = Address('Europe', 'England', 'London')
cust = Customer('Steve', 30, add)
cust.print_address() # Europe England London
cust.edit_profile('Travis', 25, 'Asia', 'China', 'Beijing')
cust.print_address() # Asia China Beijing

# -------------------------------------------------------------------------------------------------------------------

# Inheritance

# Example: User and Student

# Parent
class User:

    def __init__(self):
        self.name = 'Sam'
        self.age = 25

    def login(self):
        print('Logged In')

# Child
class Student(User):

    def enroll(self):
        print('Enrolled')

u = User()
s = Student()
print(s.name, s.age) # Sam 25
s.login() # Logged In
s.enroll() # Enrolled

# What gets inherited?
# - Constructor
# - Non Private Attributes
# - Non Private Methods

# If both parent and child have constructor then the constructor of child is executed and constructor of parent is not executed
# If child doesn't have constructor then the constructor of parent is executed just like the above code

# Constructor example 1

class Phone:

    def __init__(self, price, brand, camera):
        print('Inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Phone bought')

class SmartPhone(Phone):
    pass

s = SmartPhone(5000, 'Apple', '50MP') # Inside phone constructor
s.buy() # Phone bought


# Constructor example 2
class Phone:

    def __init__(self, price, brand, camera):
        print('Inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):

    def __init__(self, os, ram):
        print('Inside SmartPhone constructor')
        self.os = os
        self.ram = ram

s = SmartPhone('IOS', '31GB') # Inside SmartPhone constructor
print(s.os) # IOS
# Since only the child constructor is executed, s cannot access the attributes of Phone because they are not yet initialized
# print(s.price) # AttributeError: 'SmartPhone' object has no attribute 'price'


# Child cannot access private members of parent 
class Phone:

    def __init__(self, price, brand):
        print('Inside phone constructor')
        self.__price = price
        self.brand = brand

    # getter
    def get_price(self):
        return self.__price
    
class SmartPhone(Phone):

    def show_price(self):
        print(self.__price) 

s = SmartPhone(5000, 'Apple') # Inside phone constructor
# s.show_price() # AttributeError: 'SmartPhone' object has no attribute '_SmartPhone__price'
print(s.get_price()) # 5000


# Example 3
class Parent:

    def __init__(self, num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self, val, num):
        self.__val=val

    def get_val(self):
        return self.__val
        
son = Child(100,10)
# print("Parent: Num:",son.get_num())  # AttributeError: 'Child' object has no attribute '_Parent__num
print("Child: Val:",son.get_val()) # Child: Val: 100


# Example 4
class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("class A :", self.var1) # self.var1 is not same as var1 passed in the argument. They are independent of one another

class B(A):
  
    def display2(self, var1):
        print("class B :", self.var1)

obj = B()
obj.display1(200) # class A : 100
obj.display2(200) # class B : 100


# ---------------------------------------------------------------------------------------------------------------------
# Method Overriding
# If same method exist in both parent and child then the method of child class is executed
# This is called Method Resolution Order
# The order is Child → Parent → object
# i.e the method of child is executed instead of parent method because child method has higher priority

class Phone:

    def __init__(self):
        print('Inside Phone constructor')

    def buy(self):
        print('Inside the phone buy method')


class SmartPhone(Phone):

    def buy(self):
        print('Inside SmartPhone buy method')

s = SmartPhone() # Inside Phone constructor
s.buy() # Inside SmartPhone buy method
print('*' * 20)

# -----------------------------------------------------------------------------------------------------------------------

# Super keyword
# Super keyword is used inside the class to access the parent class from the child class but parent class cannot access child class
# It cannot be used outside the class
class Phone:
    
    def __init__(self):
        print('Inside Phone constructor')

    def buy(self):
        print('Inside Phone buy method')

class SmartPhone(Phone):

    def buy(self):
        print('Inside SmartPhone buy method')
        super().buy() # Calling buy memthod of Phone class using super()


s= SmartPhone() # Inside Phone constructor
s.buy()
# Inside SmartPhone buy method
# Inside Phone buy method


# Can super access parent class data: Only the class variables but not the instance variable
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # print(super().brand) # AttributeError: 'super' object has no attribute 'brand'
        # self can be used in such cases

s=SmartPhone(500000, "Apple", 15)

s.buy()



# Super can be used to access the class variables but not instance variables
# Self is used to access instance variables
class Phone:

    count = 0
    
    def __init__(self):
        print('Inside Phone constructor')

    def buy(self):
        print('Inside Phone buy method')

class SmartPhone(Phone):

    def buy(self):
        print('Inside SmartPhone buy method')
        super().buy()
        print(super().count)

s = SmartPhone() # Inside Phone constructor
s.buy()
# Inside SmartPhone buy method
# Inside Phone buy method
# 0

# super is mostly used inside the constructor of child class to initialize the attributes of parent class
# When super is encountered inside the child class, it executes the code inside the parent constructor then the program flow returns back to the child constructor
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print('Inside SmartPhone constructor')
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram

s = SmartPhone(200000, 'Vivo', '100MP', 'Android', '256GB')
# Inside SmartPhone constructor
# Inside phone constructor


# Inheritance in summary
# A class can inherit from another class.
# Inheritance improves code reuse
# Constructor, attributes, methods get inherited to the child class
# The parent has no access to the child class
# Private properties of parent are not accessible directly in child class
# Child class can override the attributes or methods. This is called method overriding
# super() is an inbuilt function which is used to invoke the parent class methods and constructor

# super(): Example 1
class Parent:

    def __init__(self, num):
      self.__num = num

    def get_num(self):
      return self.__num

class Child(Parent):
  
    def __init__(self, num, val):
      super().__init__(num)
      self.__val = val

    def get_val(self):
      return self.__val
      
son = Child(100, 200)
print(son.get_num()) # 100
print(son.get_val()) # 200


# Example 2
class Parent:

    def __init__(self):
        self.num = 100

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.var = 200
        
    def show(self):
        print(self.num)
        print(self.var)

son = Child()
son.show()
# 100
# 200


# Example 3
class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent:",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print("Child:",self.__var)

obj = Child()
obj.show() # Child: 10
# The method of child class is executed

#-------------------------------------------------------------------------------------------------------------------------------------
# Types of Inheritance
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Hierarchical Inheritance
# 4. Multiple Inheritance(Diamond Problem)
# 5. Hybrid Inheritance


# 1. Single Inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(200000, "Apple","50px").buy()
# Inside phone constructor
# Buying a phone


# 2. Multilevel Inheritance
#  class A -----> class B ------> class C
# One class can be parent and child at the same time

class continent:

    def continent_name(self):
        print('You are inside continent')

class country(continent):

    def __init__(self, name):
        print('Inside country constructor')
        self.name = name

    def country_name(self):
        print('Inside {} method'.format(self.name))

class city(country):

    def city_name(self):
        print('Inside city')

c  = city('China') # Inside country constructor
c.city_name() # Inside city
c.country_name() # Inside China method
c.continent_name() # You are inside continent


# 3. Hierarchial Inheritance
# Multiple child classes inherit from same parent class

#          ___-------> class B
#  class A
#         \___-------> class C

# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

s = SmartPhone(10000, 'Apple', '50MP') # Inside phone constructor
s.buy() # Buying a phone
f = FeaturePhone(200000, 'Vivo', '100MP') # Inside phone constructor
f.buy() # Buying a phone


# 4. Multiple inheritance
# A child class inherits from multiple parent classes

# class A-----_
#              > class C
# class B-----/

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Phone bought')

class Product:

    def review(self):
        print('Customer Review')

class SmartPhone(Phone, Product):
    pass

s = SmartPhone(200000, 'Apple', '50MP') # Inside phone constructor
s.buy() # Phone bought
s.review() # Customer Review
print()


# the diamond problem
# What happens when same method is present in both parent classes from which a child class inherits from
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# MRO - Method Resolution Order
class SmartPhone(Phone, Product):
    pass

s = SmartPhone(20000, "Apple", 12) # Inside phone constructor
s.buy() # Buying a phone
print()
# Here the buy method of Phone class is executed since it appears first in the SmartPhone(Phone, Product)
# In case of method name conflict, the class which is written first inside the () is executed


# Same code but Product is written first
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# MRO - Method Resolution Order
class SmartPhone(Product, Phone):
    pass

s = SmartPhone(20000, "Apple", 12) # Inside phone constructor
s.buy() # Product buy method


# Example 1
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):
  
    def m2(self):
        return 20
obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m1() + obj3.m1()+ obj3.m2()) # 20(A)+30(B)+20(C) = 70

#-----------------------------------------------------------------------------------------------------------------------
# Polymorphism
# Method Overriding
# Method Overloading
# Operator Overloading

# Method with same name having different arguments cannot be used in python 
# This feature is avialable in c++ and Java but not in python

class FindArea:

    def area(self, r):
        return 3.14 * r * r
    
    def area(self, l, b):
        return l*b
    
a = FindArea()
# a.area(4) #  FindArea.area() missing 1 required positional argument: 'b'
# Python only considers the recent method so only the rectangle area can be calculated using area method in the above code
print(a.area(5, 6)) # 30

# To solve this problem

class FindArea:

    def area(self, l, b=0): # Here b is the default value if b is not provided
        if b == 0:
            return 3.14 * l * l
        else:
            return l * b
        
a = FindArea()
print(a.area(1)) # 3.14
print(a.area(5, 6)) # 30

# Operator Overloading
str1 = 'python'
str2 = 'programming'
print(str1 + ' ' + str2) # python programming
print(10 + 20) # 30
# Here same operator serves different purpose

print([1, 2, 3] + [4, 5]) # [1, 2, 3, 4, 5]




    



