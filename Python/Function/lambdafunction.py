# lambda function
# Format: output = lambda X(input): Expression(function, methods, loops etc...)

# use the lambda function to multiply any number by 2
answer = lambda x: x*2
print(answer(5)) # 10

# lambda function for adding two numbers
result = lambda x,y: x + y
print(result(2.2, 3.3)) # 5.5
print(result(2,3)) # 5

# Checking conditions using lambda
check = lambda word: word in 'lambda'
print(check('a')) # True
print(check('z')) # False

# Using lambda function together with map
# Clean the given strings into float
prices = ['$10.11', '$15.15', '$50.00', '$100.00']
print(list(map(lambda price: float(price.replace('$','')), prices))) # [10.11, 15.15, 50.0, 100.0]

# Using lambda function together with map
prices = [100, 120, 50, 30, 200]
# Remove all prices less than 100
print(list(filter(lambda price: price >= 100, prices))) # [100, 120, 200]


# Keep only the students with scores higher than 70
students = [['luffy', 90],
            ['zoro', 85],
            ['coby', 50]]
# In case of nested lists, it is processed row wise so write the code accordingly
print(list(filter(lambda row: row[1] > 70, students))) # [['luffy', 90], ['zoro', 85]]
# Here, in the above code, since the students is processed row wise inside the lambda function, and the score is in the 1 index position
# so, row[1] is used inside the comparision section to locate and compare the score

students = [['Alex', 40],
            ['Broad', 70],
            ['Alan', 60],
            ['Dany', 30]]
# Keep only students with names starting with 'A'
print(list(filter(lambda row: row[0].startswith('A'), students))) # [['Alex', 40], ['Alan', 60]]


# Using lambda together with sorted using (key = ) inside sorted
words = ["apple", "kiwi", "banana", "fig"]
# Sort the given list of strings by length

# Default sort without using lambda function
sorted_words = sorted(words)
print(sorted_words) # ['apple', 'banana', 'fig', 'kiwi']

sorted_words = sorted(words, key = lambda word: len(word))
print(sorted_words) # ['fig', 'kiwi', 'apple', 'banana']

# Sort in Descending order
sorted_words = sorted(words, key = lambda word: len(word), reverse = True)
print(sorted_words) # ['banana', 'apple', 'kiwi', 'fig']


