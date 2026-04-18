import logging
import logging.config

import yaml

logger = logging.getLogger('app')

def configure_loggers():
    with open('logger_config.yaml', 'r', encoding = 'utf-8') as f:
        config = yaml.safe_load(f) # Similar to json.load()
    
    logging.config.dictConfig(config) # Using dictconfig to configure the loggers beacuse the logger configuration has to be in dict format


def main():
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')


if __name__ =='__main__':
    configure_loggers()
    main()
# Output:
# SIMPLE FORMATTER: 2026-04-18 12:51:45,568 | app | INFO | This is info message
# SIMPLE FORMATTER: 2026-04-18 12:51:45,568 | app | WARNING | This is warning message



# Here, in the config file, app logger doesnot have any handlers but the root logger has
# app logger -> handler = none, level = info
# root logger -> handler = console, level = debug

# So the messages below info are ignored by the filter of app logger
# Even though there is a debug filter in root logger, the debug log is not executed because it it ignored by the app logger
# which has a info level filter and the debug log is not propagated to the root logger


# Conclusion:
# When a message propagates, the parent logger's (Root) level filter is ignored.
# Propagation skips the level check of the parent and goes straight to the parent's handlers.
# The parent handlers can apply filters but the parent logger's filter is ignored.


# Now if the config is changed to:
# app logger -> handler = None, level = info
# root logger -> handler = console, level = critical

# The output will be:
# SIMPLE FORMATTER: 2026-04-18 13:21:11,072 | app | INFO | This is info message
# SIMPLE FORMATTER: 2026-04-18 13:21:11,072 | app | WARNING | This is warning message

# this is because the parant's logger level filter is ignored
# The app logger only allows the passage of info and warning
# The root logger doesn't have any filter in handler so both info and warning logs are executed
