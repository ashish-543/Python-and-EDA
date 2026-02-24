print("Hi \"Python\"") # Use escape character (backslash) to print ""

name = 'python'
print(type(name))

# Fomatted print 
print('The language is', name) # Normal print 
print(f'The language is {name}') # Formatted print
print(f'python {{python code}}')
print(f"2 + 3 = {2 + 3}") # 2+3 = 5


# converting integer data type to string in order to concatenate two strings
age = 23
print('Your age is: ' + str(age))

print(name * 5)
# repeats text

password = '123457879##@#'
print(len(password))

if len(password) < 8:
    print('Invalid password')


# Counting substrings.
# Count function is case sensitive.
text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""
print(text.count('Python')) # count = 2
print(text.count('python')) # count = 1


# Replacing Characters

phone = '+977-98989898'
print(phone.replace('+', '')) # output: 977-98989898 i.e replacing + with blank character

# We can also use multiple replace function to replace multiple characetrs
phone1 = '+977-433434344:'
print(phone1.replace('+', '').replace('-','').replace(':',''))


# Combining Strings
folder = 'C:/Users/Microsoft/'
file = 'python.csv'
full_file_path = folder + file
print(full_file_path)


# Splitting Substrings
stamp = "2026-09-20 14:30"
print(stamp.split(" ")) # Splits the substrings and makes a list of substrings: ['2026-09-20', '14:30'] 

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(',')) # ['1234', 'Max', 'USA', '1970-10-05', 'M']

# Indexing and Slicing
text = 'python'
print(text[2])
print(text[-4]) # The negative indexing start from the right side with a value of -1

date = "2026-09-20"
print(date[0:4]) # [a,b] behaves as [) i.e it includes the left border but right border is not included
print(date[5:7]) # Month
print(date[-2:]  ) # Day
# [a:] means that include everyting in the right side of a including a.


# Whitespace cleanup
text = '  python'
print(text.lstrip()) # lstrips the left blankspaces in a string, output= 'python'

text = 'python   '
print(text.rstrip())# output= 'python'

text = '  python  '
print(text.strip()) # To strip both left and right blackspaces, use .strip(), output = 'python'

text = 'pyt hon'
print(text.strip()) # output = 'pyt hon', .strip() cannot remove spaces in between the texts.

# .strip() can also be used to strip characters not just blank spaces.
text = '***python**'
print(text.strip('*')) # Output = 'python'

text = "python PROGRAMMING"
print(text.lower())  # ➜ python programming
print(text.upper())  # ➜ PYTHON PROGRAMMING

# lower and strip functions used together
search = "Email ".lower().strip()
data = " emAil".lower().strip()
print(search == data)  # ➜ True


# Search Functions : startswith, endswith and in
phone = "+48-176-12345"
print(phone.startswith('+48')) # True
print(phone.endswith('345')) # True
print('-' in phone) # True


# Partial Extraction Using find()
# Use find to locate where the number actually starts ignoring the country code.
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1.find('-')) # Output: 3

# Print the phone numbers without the country codes.
print(phone1[(phone1.find('-') + 1):])
print(phone2[(phone2.find('-') + 1):])
print(phone3[(phone3.find('-') + 1):])


# Input:  "968-Maria, ( D@ta Engineer );; 27y"
# Goal:   name: maria | role: data engineer | age: 27

clean = "968-Maria, ( D@ta Engineer );; 27y"
print(clean.replace('968-', 'name: ').replace(',','').replace('(', '| role:').replace(')', '|').replace('@', 'a').replace(';;', ' age:').replace('y', '').lower())
# Output : name: maria | role: data engineer | age: 27

Goal = clean.replace('968-', 'name: ').replace(',','').replace('(', '| role:').replace(')', '|').replace('@', 'a').replace(';;', ' age:').replace('y', '').lower()
print(Goal)
# Output: name: maria | role: data engineer | age: 27








