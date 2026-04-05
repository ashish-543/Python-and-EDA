# Working of an ATM using class

# Use pascal case for writing the name of any class
# ClassName

class Atm:

    # Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        # print(id(self)) # 2156543506048
        #self.menu()
    
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
        self.pin = user_pin

        user_balance = int(input('Enter your balance: '))
        self.balance = user_balance

        print('Pin created successfully')

        self.menu()


    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.pin:
            new_pin = input('Enter your new pin: ')
            self.pin = new_pin
            print('Pin updated successfully')
        else:
            print('Pin didnot match')

        self.menu()


    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your blanace is', self.balance)
        else:
            print('Pin didnot match')

        self.menu()


    def withdraw(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            amount = int(input('Enter amount to withdraw: '))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Balance withdraw successfull')
                print('Remaining balance is', self.balance)
            else:
                print('Balance not sufficient')
        else:
            print('Pin didnot match')

        self.menu()


obj1 = Atm()
print(id(obj1)) # 2156543506048
# Here the id of self and obj1 is same so it shows that self and obj1 are same thing
# In oop, a method cannot directly call another method inside a class and only objects can access the data and methods
# So to solve this problem, self is used.
# So, self is the current object
# You can use any name inplace of self

#------------------------------------------------------------------------------------------------------------------------
# Magic methods
# magic methods stars and end with __
# constructor is a magic method
# All the magic method have a specific superpower
# For example, the superpower of constructor is that, it doesnot have to be called to execute the code inside it

# Creating our own data type Fraction
class Fraction:

    # parameterized constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y

    
    # To display the new data type, __str__ is used which automatically gets executed when an object is passed to print function
    # Magic function
    def __str__(self):
        # It returns the format of new data type or the object
        return f'{self.num}/{self.den}'
    

    # This magic function is executed when + is used between objects
    # Takes two arguments, self = first fraction and other = second fraction
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_div = self.den * other.den

        return f'{new_num}/{new_div}'
    

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        return f'{new_num}/{new_den}'
    

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return f'{new_num}/{new_den}'
    

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return f'{new_num}/{new_den}'

obj1 = Fraction(3, 4)
# print(obj1) # <__main__.Fraction object at 0x000002BEBFF87920>. -> without using magic function
obj2 = Fraction(2, 3)
print('The two fractions are: {} and {}'.format(obj1, obj2)) # The two fractions are: 3/4 and 2/3
print(obj1 + obj2) # 17/12
print(obj1 - obj2) # 1/12
print(obj1 * obj2) # 6/12
print(obj1 / obj2) # 9/8
# This concept is same as operator overloading 



