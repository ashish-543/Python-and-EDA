# For else loop
# For else loop is used to check the completion of the for loop.
# For-else is used in combination with break only. Without break, the for-else doesnot serve any purpose.
# The else statement is executed only after the completion of all the iterations of the loop
# If any iteration of the loop in not completed, then the else is not executed
# SO the for-else asts acts as the if else 
# If(loop completed) -> else is executed otherwise break is executed.
# The else statement is written in the same level as for but not inside the for loop


# Check if the list contains any even number

items = [1, 3, 5, 6, 7]

for item in items:
    if item % 2 == 0:
        print('Even number encountered')
        break
else:
    print('No even number encountered')
# output: Even number encountered


# Real world use-cases:
# 1. To check missing values

names = ['harry', 'cole', 'eden', None, 'james']

for name in names:
    if name is None:
        print('Name is None')
        break
else:
    print('No None encountered')


# 2. Check if all files are .csv

files = [
    'data1.csv',
    'data2.csv',
    'data3.pdf',
    'data4.txt'
]

for file in files:
    if not file.endswith('.csv'):
        print('Non csv file encountered')
        break
else:
    print('All the files are .csv')


# Check whether any filename appears more than once
# print Duplicate found if any duplicate is found

files = [
    'report.csv',
    'data1.csv',
    'summary.csv',
    'report.csv',
    'data2.csv'
]

for file in files:
    if files.count(file) > 1:
        print(f'Duplicate of {file} found')
        break
else:
    print('No duplicate found')
# output: Duplicate of report.csv found
