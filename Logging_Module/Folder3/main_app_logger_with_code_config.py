import logging
# Although you can configure logger using this method, it is not recommended

import sys

def configure_logger():
    root_logger = logging.getLogger()
    app_logger = logging.getLogger("app")
    print("app_logger id:", id(app_logger))

    # Defining handler
    stream_handler = logging.StreamHandler(stream = sys.stdout)
    simple_formatter = logging.Formatter(
        "SIMPLE FORMATTER: %(asctime)s | %(name)s | %(levelname)s | %(message)s",
        style = "%"
    )

    stream_handler.setFormatter(simple_formatter)
    root_logger.addHandler(stream_handler)
    root_logger.setLevel(logging.DEBUG)

    app_logger.setLevel(logging.INFO)

def main():
    logger = logging.getLogger("app")
    print("app_logger id:", id(logger))
    logger.debug("This is debug message")
    logger.info("This is info message")
    logger.warning("This is warning message")

if __name__ == "__main__":
    configure_logger()
    main()


# Output:
# app_logger id: 2714235095376
# app_logger id: 2714235095376
# SIMPLE FORMATTER: 2026-04-18 18:08:56,583 | app | INFO | This is info message
# SIMPLE FORMATTER: 2026-04-18 18:08:56,583 | app | WARNING | This is warning message

# Here the id of the logger object having same name is same throughout the code
# This is because logger objects are singleton objects
# i.e no matter where you create or access a logger with the same name, same logger is referenced


# So the general steps are:
# 1. First create logger objects
# 2. Then create handlers using handler classes
# 3. Then create the formatters
# 4. Then set the formatters for handlers
# 5. Add the handlers for loggers
# 6. Set the levels of loggers




