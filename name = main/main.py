import hello # This executes all the code of hello if name = main condition is not used

print('This is inside', __name__)

hello.welcome()

# When a file is imported eg: hello.py and the file main.py is executed then first all the code of hello.py is executed then
# the code of main.py is exxecuted and for the code inside hello.py, __name__ = hello
# So to run only the necessary code of hello, all the other code is written after name = main condition

# When the import is encountered, it first executes all the code from the hello.py which lies outside the name = main condition
# Then remaining code of main.py is executed

# When the above code is executed and the __name__ == __main__ condition is not present inside hello.py, then the optput will be
# This is inside hello
# Happy New Year
# This is inside __main__
# Happy New Year


# When the above code is executed and the __name__ == __main__ condition is present inside hello.py, then the optput will be
# This is inside __main__
# Happy New Year


# So before importing from other python files check whether the code is written inside name = main or not
# If name = main is not used then the whole code of the other file is executed and that code might cause severe damage in the system
