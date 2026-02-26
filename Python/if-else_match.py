Score = 0
submitted_score = False

if Score >= 90 and submitted_score:
    print('A+')
elif Score >= 90:
    print('A')
elif Score >= 80:
    print('B')
elif Score >= 70:
    print('C')
elif Score >= 60 or submitted_score:
    print('D')
else:
    print('F')

# Check for email the following conditions:
# 1. Email must not be empty.
# 2. Email must contain a '.' and '@'
# 3. Email must contain exactly one '@' symbol.
# 4. Email must end with '.com', '.org' or '.net'
# 5. Email must not be longer than 254 characters.
# 6. Email must start and end with a letter or digit 

email = '3Sasas@gmail.com'

if email is None or email == '':
    print('Email is empty')
elif not ('.' in email and '@' in email):
    print('Email doesnot contain \'.\' or \'@\'')
elif email.count('@') != 1:
    print('There are multiple @ in the email')
elif not email.endswith(('.com', '.org', '.net')):
    print('Email doenot start with .com .org or .net')
elif len(email) > 254:
    print('Email is longer than 254')
elif not (email[0].isalnum() and email[-1].isalnum()):
    print('Email doesnot start or end with alphanumeric character')
else:
    print('Email is perfectly fine')


print('-' * 20)
# Check for password the following conditions
# 1. Must not be empty
# 2. Must be at leat 8 characters
# 3. Must include at least 1 uppercase
# 4. Must include at least 1 lowercase
# 5. Must not be same as the email
# 6. Must not contain any spaces
# 7. Must start and end with a letter or digit

password = '12121rasaQ'
upper_count = 0
lower_count = 0
for s in password:
    if s.isupper() is True:
        upper_count += 1
    if s.islower() is True:
        lower_count += 1

print(f' uppercase: {upper_count} lowercase: {lower_count}')

if password is None or password == '':
    print('Password cannot be empty')
elif len(password) < 8:
    print('Password must have at least 8 characters')
elif upper_count < 1:
    print('Password must have atleast 1 uppercase character')
elif lower_count < 1:
    print('Password must have at least 1 lowercase character')
elif password == email:
    print('Password cannot be same as email')
elif (' ' in password):
    print('Password mustnot contain any spaces')
elif not (password[0].isalnum() and password[-1].isalnum()):
    print('Password must start and end with letter or number')
else:
    print('Password is valid')

print('-' * 20)
# Inline Ifelse
# Used for simple condition check
# If condition to be checked is complex then use normal if-else statement
grade = 'A' if Score >= 90 else 'B' if Score >= 89 else 'C'
print(grade)


print('-' * 20)
# Match-Case
# Print the short form of countries

country = 'France'

match country:
    case 'Germany':
        print('DE')
    
    case 'USA':
        print('US')
    
    case 'Australia':
        print('AU')

    case 'Nepal':
        print('NP')

    case 'China':
        print('CN')

    # For default nomatch condition, use undersore
    case _:
        print('Unknown Country')
    
