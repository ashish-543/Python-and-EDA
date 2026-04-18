# This is similar to main_app_logger_with_yaml_config but the propagate is false for app logger
# This is a bit more clean and better practices are implemented in this code
# It uses logger_config1.yaml for logging configuration

import logging
import logging.config

import yaml

logger = logging.getLogger('app')

def configure_loggers():
    with open('logger_config1.yaml', 'r', encoding = 'utf-8') as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)


def main():
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
    logger.error('This is error message')

if __name__ == '__main__':
    configure_loggers()
    main()
# Output:
# This is warning message
# This is error message

# root_logger -> level = warning, handler = console
# app_logger -> level = debug, handler = None

# since the level of app_logger is debug so all the above messages are passed by app_logger
# But the propagate = false for app_logger so the logs are not passed to the root logger
# So, the app_logger behaves as logger with no handler. In such case, the lastResort handler is executed
# The last resort handler has log_level of warning

# So in the above code only the warning and above levels are executed
# Only the message is printed in the console instead of the defined output format

# Now if logging.lastResort = False
# then the output will be : No handlers could be found for logger "app"

# But if the app logger has critical log_level then all of the above logs are rejected and no outout is seen in the console



