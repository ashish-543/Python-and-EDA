import logging
import logging.config

import yaml

logger = logging.getLogger("app")

def configure_logger():
    with open("logger_config.yaml", "r", encoding = "utf-8") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)


def main():
    for i in range(100):
        logger.warning("This is warning message with number: %d", i) # Always use placeholder before passing arguments
        # logger.warning("This is warning message with number:", i) # This throws error


if __name__ == "__main__":
    configure_logger()
    main()

# If this code is run then because the backupCount = 3, three backup files with names original_file_name.(1,2,3) are created
# The flow of the program is:
# 1. First this message 2026-04-19 10:48:30,548 | app | main | WARNING | rotating_file_handler | This is warning message with number: 0
#    is stored in the file app_log.log
# 2. Then the messages keep on being stored in the file until it reaches its maximum size which is 1000 Bytes
# 3. Then a new file is created with the name app_log.log.1 in which the logs inside the app_log.log are pushed 
# 4. Then the new logs are stored in the app_log.log until it again reaches its max size
# 5. After which the logs of app_log.log are pushed to app_log.log.1 and the previous logs of app_log.log.1 are pushed to
#    another new file named app_log.log.2
# 6. Then the app_log.log contains the most recent logs, app_log.log.1 contains second most recent logs and so on
# 7. Once the new logs exceed the space in each files, the old logs are discarded


# In the above example, the file app_log.log.3 has logs starting from 72:
# 2026-04-19 10:48:30,532 | app | main | WARNING | rotating_file_handler | This is warning message with number: 72
# All the previous logs (0 - 71) are discarded due to the lack of memory assigned to each of the files




