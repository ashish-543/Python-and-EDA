# created using ()
# Ordered: No default sorting of data. Stored in same order as stored
# Indexed: Data can be accessed using indexes
# Allows Duplicates
# Mutable

my_tuple = (10, 30, 20, 10)
print(my_tuple) # <class 'tuple'>

# Allows duplicates and Ordered
print(type(my_tuple)) # (10, 30, 20, 10)

# Indexed
print(my_tuple[1]) # 30

# Immutable
my_tuple[0] = 50 # 'tuple' object does not support item assignment
my_tuple.add(60) # 'tuple' object has no attribute 'add'
my_tuple.remove(50) # tuple' object has no attribute 'remove'


# The data inside the tuple can be sorted using the sorted but the sorted data will be converted to list
print(list(sorted(my_tuple))) # [10, 10, 20, 30]

# Use Cases:
# It is used to store sensitive data that cannot be changed

