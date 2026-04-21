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
    logger.info("This is info message with arguments:", extra = {"arg1": 100, "arg2": "Hello"}) # Pass the extra paramters as dictionary
    time.sleep(1)
    logger.warning("This is warning message with arguments:", extra = {"arg1": 200, "arg2": "hello"})

if __name__ == "__main__":
    configure_logger()
    main()

# Output in the console:
# 2026-04-21 10:04:19,892 | app | INFO | This is info message with arguments: | main | {"arg1": 100, "arg2": "Hello"}
# 2026-04-21 10:04:20,901 | app | WARNING | This is warning message with arguments: | main | {"arg1": 200, "arg2": "hello"}

# Since in the above example, arg1 is always an integer value so the config file has %d for argument1
# If you are not sure about the data type of the argument then better to use %s 
