# This is the same program as multiple_handler.py but with exception
# When exceptions occur, the exceptions are emitted with the logs.
# Along with exceptions, the traceback information(diagnostic report) of the exceptions are also emitted which are saved in the files
# This breaks the structured data inside the file which is JSON in our case

import logging
import logging.config
import yaml
import time

logger = logging.getLogger("app")

def configure_logger():
    with open("log_config.yaml", "r", encoding = "utf-8") as f:
        config = yaml.safe_load(f)
    
    logging.config.dictConfig(config)

def main():
    logger.info("This is info message")
    time.sleep(0.5)
    logger.error("This is error message")

    time.sleep(0.5)
    try:
        raise TypeError("TypeError has occured")
    except:
        logger.exception("Exception has occured") # It emits the exception as logs
        # Here logger.exception captures the traceback information of an error and sends it together with logs
        # logger.exception() always logs the exception message to the default error level i.e same as logger.error()

if __name__ == "__main__":
    configure_logger()
    main()

# Output inside console:
# 2026-04-19 12:49:30,064 | app | ERROR | main | This is error message
# 2026-04-19 12:49:30,565 | app | ERROR | main | Exception has ocured
# Traceback (most recent call last):
#   File "d:\Logging Module\Folder_6\multipe_handlers_with_exception.py", line 26, in main
#     raise TypeError("TypeError has occured")
# TypeError: TypeError has occured


# Output inside file:
# {"Time": "2026-04-19 12:49:29,559", "LoggerName": "app", "Level": "INFO", "Message": "This is info message"}
# {"Time": "2026-04-19 12:49:30,064", "LoggerName": "app", "Level": "ERROR", "Message": "This is error message"}
# {"Time": "2026-04-19 12:49:30,565", "LoggerName": "app", "Level": "ERROR", "Message": "Exception has ocured"}
# Traceback (most recent call last):
#   File "d:\Logging Module\Folder_6\multipe_handlers_with_exception.py", line 26, in main
#     raise TypeError("TypeError has occured")
# TypeError: TypeError has occured

# It can be seen that, when an exception occurs, it breaks the structured nature of data inside the file
