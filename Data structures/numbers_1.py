x = 4
y = 5.5
z = 4 + 5j

print(type(x)) # integer
print(type(y)) # float
print(type(z)) # complex

# Converting string number to number
a = '55'
print(type(a)) # str
print(type(int(a))) # integer

# Converting float to integer by removing all the decimals and considering only the integer part
X = 5.5
print(int(5.5)) # output: 5

# Converting integer  -> Float
x = 5
print(float(x)) # output: 5.0

# Converting integer -> Complex
a = 3
b = 4
print(complex(a,b)) # otput: 3+4j

# Operators
print(7 / 2) # otput: 3.5
print(7 // 2) # // means floor division which means that the output is rouded to the floor value i.e lesser value
# Output: 3

print(7 % 2) # output: 1

# power operator
print(2 ** 4) # output: 16

# x = x + 3 is same as X += 3
x = 1
x = x + 3
print(x) # output: 4
x = 1
x += 3
print(x) # output: 4

# Absolute value
x = -4
print(abs(x)) # output: 4

# Rounding up numbers using floor, ceil and round. The math module must be imported to use the floor and ceil but not for round.
# floor
import math
x = 2.3434343
print(math.floor(x)) # output: 2
x = 2.5
print(math.floor(x)) # output: 2

# ceil
x = 2.3434343
print(math.ceil(x)) # output: 3
x = 2.5
print(math.ceil(x)) # output:3

# round
x = 2.3434343
print(round(x)) # round rounds up the number to the closest value
# But if the number is in middle then it rounds the number to the even value
x = 2.5656565
print(round(x)) # output: 3

x = 2.5
print(round(x)) # output: 2, since 2 is an even number

x = 3.5
print(round(x)) # output: 4, since 4 is an even number

# rounding to specific decimal places
x = 2.3434343
print(round(x, 2)) # output: 2.34, rounded to two decimal places

# truncating the decimals and only showing the integer value
x = 2.343434
print(math.trunc(x)) # output: 2
# trunc and int do the same thing
x = 2.343434
print(int(x)) # output: 2

# Generating ramdom numbers. Ramdom module must be imported for this
import random
print(random.random()) # output: 0.06753731408041397
# It generates a random floating number every time

# Generating random integer using randint(a,b) where a and b are the numbers between which random numbers are generated
print(random.randint(1,5)) # output: random number between 1 and 5 including 1 and 5


# Checking for integer
x = 2.0
print(x.is_integer()) # output: True

x = 2.1
print(x.is_integer()) # output: False

# Checking the class of variables.
x = 2.1
print(isinstance(x, int)) # False
print(isinstance(x, float)) # True
print(isinstance(x, str)) # False
print(isinstance(x, complex)) # False

# generate a random number beween 1 and 100 and check if it is even
x = random.randint(1,100)
if (x % 2) ==0:
    print(f'The number {x} is even')
else:
    print(f'The number {x} is odd')

