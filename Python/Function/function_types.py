# Types of function on the basis of action

# 1. Action Function -> Designed to perform an operation in the system instead of returning values.

# Store application log messages in a file whenever an event occurs
def write_log(message):
    with open(r'C:\Users\Vision\Desktop\app.log', 'a') as file: # r'' treats \ i.e backslash as literal character rather than escape sequence
        file.write(message + '\n')

write_log('app created') # Output inside the created file: app created
write_log('app started') # app started

#------------------------------------------------------------------------------------------------------------------
print()

# 2. Transformation function -> takes in data as input, transforms input data and returns transformed data as output

# Make a function that cleans email address and splits them into structured data like dict (username and domain) 
def split_email(email):
    clean_mail = email.strip().lower()
    username, domain = clean_mail.split('@')
    return {'username': username,
            'domain': domain}
print(split_email('  123SHHDsss@gmail.com')) # {'username': '123shhdsss', 'domain': 'gmail.com'}
print(split_email('  123SHHDsss@outlook.com')) # {'username': '123shhdsss', 'domain': 'outlook.com'}

#------------------------------------------------------------------------------------------------------------------
print()

# 3. Validation function -> Validates a condition and returns a boolean result (True or False)

# Check whether the password meets the minimum requirement of 8 characters
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password('1234ffrfr')) # True
print(is_valid_password('ddde')) # False
print(is_valid_password('12345678')) # True

# Check whether an email has a basic valid format
def is_valid_email(email):
    return '@' in email and '.' in email

print(is_valid_email('asasas@gmail.com')) # True
print(is_valid_email('asasas@gmailcom')) # False
print(is_valid_email('asasasgmail.com')) # False

#------------------------------------------------------------------------------------------------------------------
print()
# 4. Orchestrator function
# Controls program flow by calling other functions in correct order
# Represents the workflow of a program

# a. Receive an email from the user
# b. Validate an email
# c. If it is invalid, log an error in a file
# d. If it is valid, clean and structure the email
# e. Log each step of the program


# a. Receive an email from the user
write_log('Process started')
email = input('Enter your email: ')

# b. Validate an email
is_valid_email(email) # This is not necessay since email is validated in the next step

# c. If it is invalid, log an error in a file
if not is_valid_email(email):
    write_log(f'Invalid email: {email}')
else:
# d. If it is valid, clean and structure the email
    clean_email = split_email(email)
    write_log(f'Email processed: {clean_email}')
write_log('Process ended')

# e. Log each step of the program


# Now, make an orchestrator function to call all these functions

def process_user_email(email):
    write_log('Process started')
    if not is_valid_email(email):
        write_log(f'Invalid email: {email}')
    else:
        clean_email = split_email(email)
        write_log(f'Email processed: {clean_email}')
    write_log('Process ended')

# Ask for user email
email = input('Enter your email: ')

# Call orchestrator function
process_user_email(email)
