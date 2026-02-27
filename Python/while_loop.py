# While condition loop
# It is similar to for loop in the C-programming
# 1. First step is initialization of incrementor or condition checker
# 2. Next step is determining the condition for the while the loop
# 3. And the last step is adding the modifier (incrementor or decrementor or none)


# print number from 1 to 5 using for loop

i = 1
while i <= 5:
    print(i)
    i += 1
# output:
# 1
# 2
# 3
# 4
# 5


# Build a program which continuously asks opinion from the user unless the user says yes
opinion = ''
while opinion != 'yes':
    opinion = input('What is your opinion: ')
print('Thank you')
# output
# What is your opinion: no
# What is your opinion: good
# What is your opinion: not good
# What is your opinion: hi
# What is your opinion: yes
# Thank you


print('*' * 20)
# While True
# This loop does not have a condition as the other while loop
# This loop runs indefinitely until a break condition is encountered
# Do not use while true loop without using break condition

# Build the same program as above using while true loop

opinion = ''
while True:
    opinion = input('What is your opinion: ')
    if opinion == 'yes':
        break
print('Thank you')
# output:
# What is your opinion: no
# What is your opinion: not
# What is your opinion: neither
# What is your opinion: good
# What is your opinion: yes
# Thank you


# For the same program as above
# Allow upto 3 attempts
# If the user types 'yes', print 'Glad we are on the same page'
# Otherwise, print'3 strikes, you are out'

opinion = ''
i = 0
while i < 3:
    opinion = input('What is you opinion: ')
    if opinion == 'yes':
        print('Glad we are on the same page')
        break
    i += 1
else:
    print('3 strikes, You are out')
# Here else can also be used with while loop just like the for_else loop

# Diff between for and while
# for loop has a iteratable sequence, whereas while doesnot have such sequence
# for loop has a predetermined end condition which is the end of sequence, whereas while has a user defined condition
# in for loop, number of iterations is known, whereas it is not known in while loop
