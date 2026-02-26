items = (1,2,3,4,5)
for item in items:
    print(f'Round: {item}')
# Output:
# Round: 1
# Round: 2
# Round: 3
# Round: 4
# Round: 5


print('-' * 20)
# Same thing can be done for lists
items = [1,2,3,4,5]
for item in items:
    print(f'Round: {item}')


# For loop is also used to iterate through the characters in a string
text = 'terminal'
for word in text:
    print(word)
# output
# t
# e
# r
# m
# i
# n
# a
# l


# Range can also be used to deifne the range for the iterator in the loop
# range(stop) stop is the boundry. It starts from 0 and goes up to the second last number in the range
# it behaves as [0, stop) bracket.
for item in range(5):
    print(f'Round: {item}')
# output:
# Round: 0
# Round: 1
# Round: 2
# Round: 3
# Round: 4


print('-' * 20)
# Starting variable can also be added to the range. Here, the start is optional
# range(start, stop) includes [start, stop)
for item in range(1, 5):
    print(f'Round: {item}')
# output:
# Round: 1
# Round: 2
# Round: 3
# Round: 4


print('-' * 20)
# Step can also be added to the range function in order to add the step for each increment
# Step is optional.
for item in range(1, 10, 2):
    print(f'Round: {item}')
    # Since the step is 2 and the range starts from 1 so 2 is added each time which results in odd numbers from 1 to 9
# output:
# Round: 1
# Round: 3
# Round: 5
# Round: 7
# Round: 9


# Use for loop to aggregate data
# Sum

scores = [10, 20, 30, 40, 50]
total_score = 0
for score in scores:
    total_score += score
    print(f'Current Total: {total_score}')
print(f'The total score is {total_score}')


# Use for loop to transform data like cleaning data before processing
files = [' Report.csv ', 'Data.csv ', 'final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f'Processed file: {file}')
# output:
# Processed file: report.csv
# Processed file: data.csv
# Processed file: final.csv


# Print the 7-times table
# Format: 7 * 1 = 7
for number in range(1, 11):
    print(f'7 * {number} = {number * 7}')


print('-' * 20)
# Print a left aligned pyramid with 6 rows
# *
# **
# ***

for number in range(1, 7):
    print('*' * number)
