# This program contains a custom filter that filters the logs which have argument less than the threshold value.
# The custom flter is a callable that receives LogRecord as input and its computes something and finally returns True or Flase as output
# A callable is any object that can be "called" using parentheses () and potentially passed arguments, similar to function

# In this example we'll look at how to create custom filters.

# We'll set up two handlers, one of which will look for some value in the `extra` dictionary, and only handle the log
# record if that value satisfies some condition.

# Specifically we are going to configure our logger this way:
# 1. App logger will be set to WARNING
# 2. App logger wil have two handlers, the "regular" handler which will log all
#   log records it receives (INFO and up), and a "special" handler, which will
#   only handle WARNING and higher levels, as well as check that some value(s) in the `extra`
#   data meet some condition(s) before it will handle the log.

# The custom filter needs to be defined in Python code, that's not something we can
# specify in the configuration, but we will make a reference to it in the config when we attach it
# to the specific handler. Side note, you can also attach filters to the logger itself, using the same
# approach, just setting the configuration at the logger level instead of the handler level.

# This example also shows how we can pass filter configuration values from the YAML config file to the filter class
# when it gets instantiated by the logging system.

# You'll see in the configuration file that we use something weird in the filter definition: `()`.
# This is meant to be a hint to the logging system that it should instantiate the class, and pass the
# configuration.


import logging
import logging.config
import yaml
import time

logger = logging.getLogger("app")

# Creating customfilter class inside which filter function is defined
class CustomFilter(logging.Filter): # It inherits from logging.filter
    def __init__(self, arg_name: str = None, arg_threshold: int = None): # Since default value(None) are given, so object can be created without passing arguments
        self.arg_name = arg_name 
        self.arg_threshold = arg_threshold

    def filter(self, record: logging.LogRecord) -> bool: # record is an instance of LogRecord
        # Here we look for the arg attribute. If the attribute is present, and it's value
        # is > self.arg_threshold, then we allow the record to be processed (return True),
        # otherwise we filter it out (return False)
        return(
            self.arg_name # -> self.arg_name == "my_arg" # always truthy (a string) i.e it only checks if arg_name is present inside filter or not
            and self.arg_threshold # -> self.arg_threshold == 100, These values are fixed for the filter, not per log record
            and hasattr(record, self.arg_name) # -> hasattr(record, "my_arg"). 
            and getattr(record, self.arg_name) > self.arg_threshold # -> getattr() = None in first message, = 100 in second message
        )
    
def configure_logger():
    with open("logger_config.yaml", "r", encoding = "utf-8") as f:
        config = yaml.safe_load(f)
    
    logging.config.dictConfig(config)

def main():
    logger.error("Error message1: my_arg not specified")
    time.sleep(1)
    logger.error("Error message2: my_arg = 100", extra = {"my_arg": 100})
    time.sleep(1)
    logger.error("Error message3: my_arg = 200", extra = {"my_arg": 200})

if __name__ == "__main__":
    configure_logger()
    main()

# Output inside console
# 2026-04-21 13:20:41,989 | app | ERROR | main | Error message1: my_arg not specified
# 2026-04-21 13:20:43,000 | app | ERROR | main | Error message2: my_arg = 100
# 2026-04-21 13:20:44,041 | app | ERROR | main | Error message3: my_arg = 200
# Special Handling: 2026-04-21 13:20:44,041 | app | ERROR | Error message3: my_arg = 200

# So the the value of arg_name inside filter is "my_arg" so the name the extra parameter inside log message should be the same i.e "my_arg"
# After passing my_arg as extra parameter inside the message, my_arg is created inside the LogRecord
# This is accessed using the hasattr and getattr from the filter method inside the CustomFilter class
# The value of my_arg is different for each log message


# So the program flow is, 
# the filter check which variable is used for filtering from the filter inside the config file
# In our case it is "my_arg" so the fiter searches for the value of my_arg inside the record which it gets from the log message
# After performing the coputation, it returns true or false 

