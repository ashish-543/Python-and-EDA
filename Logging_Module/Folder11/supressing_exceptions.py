# This program shows how exceptions can be supressed
# Generally if logging exception occurs then it doesnot hamper the execution of application
# But it can cause unwanted information being written in files or shown in console
# This can be achieved by passing a boolean parameter inside the configure_logger function
import logging
import logging.config
import yaml
from datetime import datetime, UTC
import json

logger = logging.getLogger("app")

def serialize_local_timestamp(t: float) -> str:
    dt = datetime.fromtimestamp(t, UTC)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

class JSONFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord):
        log_dict = {
            "time": serialize_local_timestamp(record.created),
            "loggerName": record.name,
            "levelName": record.levelname,
            "levelNumber": record.levelno,
            "message": record.getMessage(),
            "module": record.module,
            "filename": record.filename,
            "filePath": record.pathname,
            "funcName": record.funcName,
            "exceptionInfo": record.exc_info,
        }

        return json.dumps(log_dict, default = str)

def configure_logger(raise_exceptions: bool = True): # Here a parameter raise_exceptions is created with a default value True
    with open("logger_config.yaml", "r", encoding = "utf-8") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)
    logging.raiseExceptions = raise_exceptions


def main():
    try:
        raise ValueError("This is a test exception")
    except ValueError:
        logger.exception("An exception occurred", stack_info = True)

    logger.info("App continues running after logging exception")

if __name__ == "__main__":
    configure_logger(raise_exceptions = False)
    main()

# Output if configure_logger()  is called without passing arguments i.e default value True
# -> It throws exception and all the debugging information is shown in the console


# Inside the filter function, if return json.dumps(log_dict, default = str) with default = str is used then the output will be:

# {"time": "2026-04-22T03:34:29.011416Z", "loggerName": "app", "levelName": "ERROR", "levelNumber": 40,
# "message": "An exception occurred", "module": "supressing_exceptions", "filename": "supressing_exceptions.py",
# "filePath": "d:\\Logging Module\\Folder_11\\supressing_exceptions.py", "funcName": "main", "exceptionInfo": ["<class 'ValueError'>",
# "This is a test exception", "<traceback object at 0x0000024AC0741EC0>"]}

# {"time": "2026-04-22T03:34:29.011416Z", "loggerName": "app", "levelName": "INFO", "levelNumber": 20,
# "message": "App continues running after logging exception", "module": "supressing_exceptions", "filename": "supressing_exceptions.py",
# "filePath": "d:\\Logging Module\\Folder_11\\supressing_exceptions.py", "funcName": "main", "exceptionInfo": null}

# In this case, the system is still supressing the exceptions but the json_formatter is formatting the exception log where it is only showing
# the mentioned fields inside the formatter and ignoring all the other debugging messages such as : TraceBack and stackTrace
# If the default = str is not used then record.exc_info is not JSON serializable so the exception log won't be shown in the console


# Conclusion:
# What the logging.raiseExceptions = False essentially does is, it ignores the dubugging messages of the exception
