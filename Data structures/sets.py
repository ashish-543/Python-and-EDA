# sets
# Created by using {}
# Unordered
# Unique
# Not Indexed
# Mutable


my_set = {10, 30, 20, 50, 10}

# Unordered and Unique

# If duplicate is encountered, it is stored and shown only once
print(my_set) # {10, 20, 50, 30}
# Here the data inside the set is stored in a random order i.e not ordered in a specific order
# So python randomly orders the data
# Unlike other datatypes, where data is stored in a sequence in memory, the data inside sets is stored in random locations using hash function
# This is done for the speed

# Not Indexed
# print(my_set[1]) # TypeError: 'set' object is not subscriptable

# Mutable
my_set.remove(50)
print(my_set) # {10, 20, 30}

a = {10, 20, 30, 40}
# Adding values to the sets
a.add(50)
print(a) # {40, 10, 50, 20, 30}

# add() only adds new value if it is unique
a.add(10)
print(a) # {40, 10, 50, 20, 30}

# update()
# Adds another group of values(iterable) into the set
a.update([1,2,3,4]) 
print(a) # {1, 2, 3, 4, 40, 10, 50, 20, 30}

a.update('python')
print(a) # {1, 2, 3, 4, 'y', 40, 10, 'n', 't', 50, 'p', 20, 'o', 'h', 30}

# add is used to insert single value into the set whereas update is used to insert multiple values into the sets


# update shortcut -> |=
a = {10, 20, 30, 40}
a |= {50,15}
print(a) # {50, 20, 40, 10, 30, 15}

# Removing values from the set
a = {10, 20, 30, 40}
a.remove(10)
print(a) # {40, 20, 30}

# removing value that doesnot exists throws error and breaks the flow of code so discard is used which doesnot throw error if value is not found
# a.remove(100) # KeyError: 100

# discard
# Remove value if it exists and does nothing if it doesnot exists
a.discard(100) # No action
print(a) # {40, 20, 30}

# pop
# It removes something totally random so use of pop is not recommended in sets
a.pop()
print(a) # {20, 30}

# Math Methods
# 1. Union -> |
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.union(b)) # {40, 10, 50, 20, 60, 30}
print(a | b) # {40, 10, 50, 20, 60, 30} -> Shortcut
print(a) # {40, 10, 20, 30}
# No change in the original values of set


# 2. Intersection
print(a.intersection(b)) # {40, 30}
print(a & b) # {40, 30}

# 3. A only (A-B)
# A-B
print(a.difference(b)) # {10, 20}
print(a - b) # {10, 20}

# B-A
print(b.difference(a)) # {50, 60}
print(b - a) # {50, 60}

# A-B union B-A
# symmetric difference
print(a.symmetric_difference(b)) # {10, 50, 20, 60}

# Relationship
# Is subset
print(a.issubset(b)) # False

a = {30, 40}
b = {30, 40, 50, 60}
print(a.issubset(b)) # True

# superset: If a is subset of b then b is superset of a
print(b.issuperset(a)) # True

# disjoint
# Returns true if both sets share no common values
print(a.isdisjoint(b)) # False
a = {10, 20}
b = {30, 40}
print(a.isdisjoint(b)) # True




