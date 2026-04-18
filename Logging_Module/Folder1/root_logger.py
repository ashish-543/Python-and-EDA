import logging

# Creating logger object
# With last resort handler on
# Last resort handler is executed when a logger doesnot have any handlers attatched to it

logger = logging.getLogger() # Since no name is specified inside getLogger(), it is a root logger
# You can name it anything, doesn't have to logger everytime

# Inspect root logger configuration
print(f'{logger.hasHandlers()=}') # logger.hasHandlers()=False
# f'{expr}' → prints value only but f'{expr=}' → prints expression + value

# Compare the level of the last resort handler and warning level
# The level of warning can be directly called using logging.WARNING
print(f'{logger.getEffectiveLevel()=}, {logging.WARNING=}') # logger.getEffectiveLevel()=30, logging.WARNING=30
# Here, the logger doesnot have any handler so the effective level of logger is the effective level of last resort handler
# which is the default warning level


# Send various level log messages to the root handler
# logging.lastResort = False # You can configure the lastresort option

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
# Ouput:
# This is warning message
# This is error message
# This is critical message

# Here, only three messages are printed which satisfy the condition: >= default level of last resort handler(warning)

# Now, if the last resort handler is turned off then
logging.lastResort = False
logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
# Output: No handlers could be found for logger "root"

# It simply prints this default message but doesnot throw any error


# Note:------------------------------------------------------------------------------------------------
# The last resort handler uses StreamHandler which uses sys.stderr (default) or sys.stdout
# StreamHandler shows the output in the console
# stdout -> normal output(print)
# stderr -> errors, logs and diagnostics
# Although they both show the information in console, both of them have different channels and different usecases
# Usually for logging, stderr is used






    


