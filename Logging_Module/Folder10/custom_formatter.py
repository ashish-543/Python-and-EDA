# A custom formatter is created in this code

import logging
import logging.config
import yaml
import json
from datetime import datetime, UTC

logger = logging.getLogger("app")


def serialize_local_timestamp(t: float) -> str: # input looks like: 1713537000.123 which is called Unix timestamp so it doesnot have any timezone 
    dt = datetime.fromtimestamp(t, UTC) # Convert timestamp → datetime in UTC format. If .fromtimestamp(t) is used then timestamp -> local datetime
    # output will be somethig like: 2026-04-19 14:30:00.123456+00:00
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ") # Format datetime → string


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        # Create a dictionary that gathers all the info we want to log
        # We'll need to make sure whatever we gather is JSON serializable (or
        #   we can alternatively create a custom JSON encoder)
        # We could even leverage Pydantic to do this for us, especially if we already use Pydantic
        #   in our application. But let's keep it simple, and just see how custom formatters work.

        # Notes:
        # The attribute record.message is the raw (non-interpolated message string). Instead, we use
        #   .getMessage() to have the log record return the interpolated message string.
        # The log creation time is available in record.created, which is a float representing the time in
        #   seconds, but as a local time. We can convert this to UTC and with whatever string serialization we want.
        # We'll want to serialize the exception info and stack trace, and although the record provides us that info,
        # we would need to serialize that ourselves - instead, we can use the Formatter class's built-in methods
        # formatException() and formatStack() to do this for us.
        log_dict = {
            "time": serialize_local_timestamp(record.created), # record.created is seconds since epoch (1970) eg: 1713537000.123  
            "loggerName": record.name,
            "levelName": record.levelname,
            "levelNumber": record.levelno,
            "message": record.getMessage(), # use getMessage() instead of message
            "module": record.module,
            "filename": record.filename,
            "filePath": record.pathname,
            "funcName": record.funcName,
            "exceptionInfo": (
                self.formatException(record.exc_info) # FormatException is inside logging.Formatter and since we are inheriting from it, we can directly use it.
                if record.exc_info # exec_info is inside record i.e in the LogRecord
                else None
            ),
            "stackTrace": (
                self.formatStack(record.stack_info)
                if record.stack_info
                else None
            )
        }

        
        # These are all the standard attributes of the LogRecord 
        # We cannot directly access the extra parameters
        #            
        # Identify attributes that were passed in extras - no direct way to do this, so we'll
        # compare what a regular log record without any extras looks like, and identify keys
        # in the current log record that are not present in the plain-vanilla log record.

        # 1. For this first create a dummy log with dummy values and convert it into dict and access only the keys
        standard_fields = logging.LogRecord("", 0, "", 0, "", (), None).__dict__.keys()

        # These are the standardfields for:
        # loggername, loglevel, filepath, linenumber, message, args and exceptioninfo
        # Even if you enter less number of attributes of LogRecord, it still creates a full set of LogRecord attributes
        # Answer: Even if you pass minimal arguments like ("", 0, "", 0, "", (), None),
        # the LogRecord class still creates all its standard attributes because they are explicitly defined in its constructor — not inferred from the inputs.

        # 2. Then convert it into dictionary and access its attributes
        for key, value in record.__dict__.items():
            if key not in standard_fields:
                log_dict[key] = value

        return json.dumps(log_dict, default = str) # json.dump() -> writes JSON directly to file
                                    # json.dumps() -> returns a JSON string
    

def configure_loggers():
    with open("logger_config.yaml", "r", encoding = "utf-8") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)

def main():
    logger.info("Message 1")
    logger.info("Message 2: val=%s", "value")
    logger.error("Message 3", extra={"a": 1, "b": 2, "c": 3})

    try:
        raise ValueError('ValueError has occured')
    except:
        logger.exception("Exception has occured", stack_info = True)


if __name__ == "__main__":
    configure_loggers()
    main()
