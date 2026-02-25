print(True)
print(False)
print(type(True)) # output: bool

# Checking if value exists
a = 123
print(bool(a)) # output: True

a = 0
print(bool(a)) # output: False, since 0 is not registed as value in boolean arithmetics

print(bool()) # output: False for empty value

print(bool(None)) # output: False for none

print(bool(' ')) # output: True for blankspace
print(bool('')) # output: False for empty string


# any() and all()

email = ''
phone = ''
username = ''
# Allow registration
# If any field is filled
print(any([email, phone, username])) # any returns True if anyone of the variable has value. The values should be provided in the form of list.
# output: False

email = '12121212@gmail.com'
phone = ''
username = ''
print(any([email, phone, username])) # output: True

# Allow registration
# Only if all fields are filled
email = '12121212@gmail.com'
phone = '2121212'
username = ''
print(all([email, phone, username])) # output: False

email = '12121212.com'
phone = '3434'
username = '4343'
print(all([email, phone, username])) # output: True since all the values exist\

# isinstance
print(isinstance(5, int)) # output: True

x = 4
print(x.is_integer()) # output: True

text = 'python'
print(text.startswith('p'))
print('th' in text)

print('-' * 20)
# Comparision Operators
print(10 == 10) # output: True
print('a' == 'a') # output: True, python compares the values alphabetically.
print('A' == 'a') # output: False since python is case sensitive

# Chained comparision
print(1 < 2 < 9) # Comparision starts from the LHS i.e 1<2 -> True and 2<9 -> True so, True and True -> True
print(2 < 1 < 9) # False 

# Is age between 18 and 30?
age = 23
print(18 <= age <= 30) # output: True
age = 30
print(18 <= age <= 30) # output: True
age = 31
print(18 <= age <= 30) # output: False


# Logical Operators
print('-' * 20)

# Check if the system is under pressure
# System is under pressure if either of the value exceeds threshold
cpu_usage = 0
memory_usage = 0
print(cpu_usage >= 90 or memory_usage >= 90) # False

cpu_usage = 20
memory_usage = 90
print(cpu_usage >= 90 or memory_usage >= 90) # True

# Checking user credentials before login
email = True
password = True
print(email and password)

email = True
password = False
print(email and password)

name = ''
print(name) # output: blankspace
print(not name) # True, since name does not have a value and not false -> True
print(not 0) # output: True


# In case of chained logical conditions, and has a higher priority than or. () has the highest priority.

# Allow access only if the user is logged in
# or they are guest
# but they mustnot be banned

logged_in = True
guest = True
banned = True
print((logged_in or guest) and not banned )
print('-' * 20)

# 1. Check if a user's name is not empty and the age is greater than or equal to 18
# 2. Check if the password is at least 8 characters long and does not contain spaces.
# 3. Check if the user's email is not empty, contains '@', ends  with '.com'
# 4. Check if a username is a string, is not None, and is longer than 5 characters.
# 5. Check if the user is either an admin or a moderator and either they're not banned and they have verified their email.

username = 'python'
age = 20
password = '12121212'
email = '12345@gmail.com'
user_status = 'admin'
banned = False
verified_email = True

print(bool(username) and (age >= 18)) # 1. output: True
# print(username and (age >= 18)) is same thing

print(len(password) >= 8 and (' ' not in password)) # 2. output: True

print(bool(email) and ('@' in email) and email.endswith('.com')) # 3. Output: True

print(isinstance(username, str) and (username is not None) and len(username) > 5) # 4. output: True

print((user_status in ['admin', 'moderator']) and not banned and verified_email) # 5. output: True


# Membership and identity operators
print('-' * 20)
print('f' in 'python') # False
print(2 in [1,2,3]) # True

# Ensure the domain is not banned
domain = 'gmail.com'
banned_domain = ['bot.net', 'spam.com', 'fake.org']
print(domain not in banned_domain) # True

# is operator
# The is operator compares the object_id of the variables instead of the values. '=' operator compares the values of the variables
# So in python, for simple variables having same values, same object_id is assigned. object_id is similar to pointer.
# So the is operator compared the object_id of the variables and the variables having same values return True
# This is done to optimize the performance, but this only happens for simple variables like integer and not for lists

a = [1,2,3]
b = [1,2,3]
print(a == b) # True since == compares the values
print(a is b) # False since is operator compares the object_id and for complex data types, the same object_id is not assigned for variables having same values
a = 555
b = 555
print(a == b) # True
print(a is b) # True

# But if = operator is used to assign the values of one variable to another then same object_id is assigned to both variables even if they are complex data types
a = [1,2,3]
b = a
print(a == b) # True
print(a is b) # True

# Check if the email exists and is not empty
email = '1234@gmail.com'
print(email is not None and email != '')
print(email is not None and bool(email))


