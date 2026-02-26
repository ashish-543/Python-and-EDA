# Break
# When break is encountered, it immediately stops the execution of current iteration of code and moves outside of the loop or block of code.


# When empty value is detected, use break.
names = ['steve', 'will', '', 'shane']
for name in names:
    print(f'Name: {name}')
# output:
# Name: steve
# Name: will
# Name:
# Name: shane


print('*' * 20)
# Solution
for name in names:
    if name == '':
        print('Empty value encountered')
        break
    print(f'Name: {name}')
# output:
# Name: steve
# Name: will
# Empty value encountered


print('*' * 20)
# Continue 
# When continue is encountered, it skips the further execution and moves to the next iteration or step.

# If empty value is encountered, skip the further execution of current iteration and move to the next iteration
for name in names:
    if name == '':
        print('Empty value encountered')
        continue
    print(f'Name: {name}')
# output:
# Name: steve
# Name: will
# Empty value encountered
# Name: shane


print('*' * 20)
# Pass
# When pass is encountered, it simply does nothing and executes the remaining part of the current iteration and moves to the next iteration
# It simply acts as a placeholder for future actions i.e we use pass to signal that action is required but the action to be taken is not currently known

for name in names:
    if name == '':
        name = name.replace('', 'unknown')
        pass  # todo: handle empty values
    print(f'Name: {name}')
# output
# Name: steve
# Name: will
# Name: unknown
# Name: shane


# Loop through a list of days and print only the working days, skipping the weekends
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
weekends = ['sat', 'sun']
for day in days:
    if day in weekends: # Try not to use lists or other data types inside loop. Using variable names is a better practice.
        continue
    print(f'Current day: {day}')
# output
# Current day: mon
# Current day: tue
# Current day: wed
# Current day: thu
# Current day: fri



# Check for malicious emails.
emails = [
    'ascsds@gmail.com',
    '223234@outlook.com',
    'DROP TABLE USERS;',
    'fgrfgrt2@gmail.com'
]
# This is an example of SQL Injection attack and since SQL statements end with ';', so when ; is encountered, stop the execution of code
for email in emails:
    if email.endswith(';'):
        print('Malicious code detected.')
        break
    print(f'Current email: {email}')
# output:
# Current email: ascsds@gmail.com
# Current email: 223234@outlook.com
# Malicious code detected.
