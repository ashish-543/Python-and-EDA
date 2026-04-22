Python Logging Project – README
Overview

This project is a structured, step-by-step exploration of Python’s logging system, progressing from basic concepts to advanced production-ready configurations. Each folder focuses on a specific concept, allowing you to build a deep understanding of logging in real-world applications—especially useful for backend systems and data engineering pipelines.

Project Structure
Folder 1: Root Logger & Last Resort Handler
Demonstrates how the root logger works by default.
Explores the lastResort handler, which prevents logs from being completely lost when no handlers are configured.
Helps you understand:
Default logging behavior
Logging levels
Why logs still appear even without configuration
Folder 2: YAML-Based Logger Configuration
Introduces configuration using a YAML file.
Uses logging.config.dictConfig() to load structured configurations.
Benefits:
Clean separation of configuration from code
Easy to maintain and modify logging settings
Folder 3: Code-Based Logger Configuration
Configures logging entirely in Python instead of YAML.
Useful when:
Dynamic configuration is needed
External config files are not preferred
Covers:
Handlers
Formatters
Logger hierarchy
Folder 4: FileHandler Setup
Writes logs to a file instead of the console.
Key concepts:
Persistent logging
Log file management basics
Folder 5: RotatingFileHandler
Prevents log files from growing indefinitely.
Automatically rotates logs based on:
File size (maxBytes)
Backup count
Critical for production systems to avoid disk space issues.
Folder 6: Multiple Handlers
Configures multiple handlers simultaneously.
Example:
Console handler for debugging
File handler for persistence
Demonstrates how different handlers can have different log levels.
Folder 7: Custom String Formatter
Customizes how logs appear.
Covers:
Log message structure
Timestamps
Log levels
Contextual information
Folder 8: Using the extra Parameter
Adds custom fields to log records.
Useful for:
Structured logging
Adding metadata (e.g., request_id, user_id)
Demonstrates how to access these fields in formatters.
Folder 9: Custom Filters
Filters log records based on custom logic.
Example use cases:
Only log messages above a dynamic threshold
Filter logs based on custom attributes
Shows how to implement filter() method effectively.
Folder 10: Custom Formatters
Extends logging.Formatter to create advanced formats.
Example:
JSON logging for structured logs
Useful for:
Log aggregation tools (ELK, Datadog, etc.)
Data pipelines
Folder 11: Suppressing Logging Exceptions (Production)
Prevents logging failures from crashing the application.

Uses:

logging.raiseExceptions = False
Important for production environments where:
Logging must never interrupt execution
Stability is prioritized over debugging visibility
