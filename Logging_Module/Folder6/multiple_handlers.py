# Make a program that emits logs in console and file
# Only the logs with level >= warning are shown in the console
# In the file, structure the data to be stored in JSON format

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

if __name__ == "__main__":
    configure_logger()
    main()

# Output in the console:
# 2026-04-19 12:35:28,285 | app | ERROR | main | This is error message

# Output inside the file:
# {"Time": "2026-04-19 12:35:27,771", "LoggerName": "app", "Level": "INFO", "Message": "This is info message"}
# {"Time": "2026-04-19 12:35:28,285", "LoggerName": "app", "Level": "ERROR", "Message": "This is error message"}

