# List comprehension is used for list operations
# It shortens the code for list operations

# It has three parts: Data Transformation, Loop and Filter
# The filter part is optional

# Normalize the given domains and store the normalized domains in another list called cleaned
domains = [' www.google.com',
           'openai.com ',
           ' localhost.com',
           'WWW.YOUTUBE.COM'
           ]

# Writing different steps in different line is recommended for list comprehension since makes the code clear.

# No need to write : after loop and if statement
cleaned = [
    domain.lower().strip().replace('www.', '')
    for domain in domains
    if '.' in domain
]
# cleaned = [domain.lower().strip().replace('www.', '') for domain in domains if '.' in domain]

print(cleaned) # ['google.com', 'openai.com', 'localhost.com', 'youtube.com']

# Without using filter
# Transforms all the elements of list.
cleaned = [
    domain.lower().strip().replace('www.', '')
    for domain in domains
]
print(cleaned) # ['google.com', 'openai.com', 'localhost.com', 'youtube.com']


# No transformation, only filtering and loop
cleaned = [
    domain
    for domain in domains
    if '.' in domain
]
# cleaned = [domain for domain in domains if '.' in domain]
print(cleaned) # [' www.google.com', 'openai.com ', ' localhost.com', 'WWW.YOUTUBE.COM']

# Using list comprehension, 3 actions can be performed:
# 1. Data Transformation + Filtering
# 2. Only data transformation
# 3. Only data filtering
