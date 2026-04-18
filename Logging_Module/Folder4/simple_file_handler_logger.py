import logging
import logging.config

import yaml

logger = logging.getLogger("app")

def configure_logger():
    with open('logger_config.yaml', 'r', encoding = 'utf-8') as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)

def main():
    logger.error("This is error message: %s %d", 'argument', 100) # Using f{} is not recommended so use % while passing arguments in the log message
    logger.warning("This is warning message: %d %s", 101, 'parameter')
    logger.debug("This is debug message")


if __name__ == "__main__":
    configure_logger()
    main()

# Output Inside File
# 2026-04-18 19:14:31,840 | app | ERROR | main | This is error message: argument 100
# 2026-04-18 19:14:31,840 | app | WARNING | main | This is warning message: 101 parameter
