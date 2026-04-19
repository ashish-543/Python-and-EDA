# Write a program that customizes the DateTime output to a normal UTC format
# UTC format: 2026-04-19T14:30:00.123Z 
# Here T is the time separator whereas Z indicates that the given time is in UTC format
# By default, logging uses local time: 2026-04-19 10:48:30,548
# This local time is the combination of two strings one that shows yy-mm-dd hh:-mm:ss and the other shows milliseconds
# i.e logging local time: Y-m-d H:M:S + milliseconds i.e concatenation of two strings


# We will specify this formater globally in the logging library
# Doing this will guarantee that the time is always formatted in UTC format

import logging
import logging.config
import yaml
import time

logger = logging.getLogger("app")

def configure_logger(): 
    with open("log_config.yaml", "r", encoding = "utf-8") as f:
        config = yaml.safe_load(f)

    # Configuring the formatter in the logging library
    logging.Formatter.converter = time.gmtime # gmtime gives the UTC time
    logging.Formatter.default_time_format = "%Y-%m-%dT%H:%M:%S" # This produces base time stamp 2026-04-19T14:30:00 
    logging.Formatter.default_msec_format = "%s.%03dZ" # The upper base time is passed inplace of %s and millisecond part is passed in place of %03d
    # where %03d Print an integer as a 3-digit number, adding leading zeros if it has fewer than 3 digits eg: 001 for 1
    # So the output from %s.%03dZ is the combination of base time an millisecond which is shown in the console
    logging.config.dictConfig(config)

def main():
    logger.info("This is info message")
    time.sleep(0.5)
    logger.warning("This is warning message")

if __name__ == "__main__":
    configure_logger()
    main()


# Output in the console:
# 2026-04-19T15:48:25.390Z | app | INFO | This is info message
# 2026-04-19T15:48:25.894Z | app | WARNING | This is warning message
