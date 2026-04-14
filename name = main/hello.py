def welcome():
    print('Happy New Year')


if __name__ == '__main__':
    print('This is inside', __name__)
    welcome()

# Here, __name__ = main if the same file is executed
# i.e if the file hello.py is executed then __name__  = __main__
# but if the hello file is imported in main and the main file is executed then the above file will result __name__ = hello

# When the above code is executed i.e hello.py file is executed, the output will be:
# This is inside __main__
# Happy New Year
