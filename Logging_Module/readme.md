# Python Logging Project

## 📌 Overview

A structured, hands-on project to learn Python logging from fundamentals to production-level practices. Each folder represents a progressive concept, helping build a complete and practical understanding of logging systems.

---

## 📁 Project Structure

```
.
├── Folder1_Root_Logger/
├── Folder2_YAML_Config/
├── Folder3_Code_Config/
├── Folder4_FileHandler/
├── Folder5_RotatingFileHandler/
├── Folder6_Multiple_Handlers/
├── Folder7_Custom_Formatter/
├── Folder8_Extra_Parameter/
├── Folder9_Custom_Filters/
├── Folder10_Custom_Formatters/
└── Folder11_Production_Settings/
```

---

## 📂 Folder Details

### 1. Root Logger & Last Resort Handler

* Understand default logging behavior
* Explore root logger and fallback (`lastResort`)
* Learn logging levels and propagation basics

---

### 2. YAML-Based Configuration

* Configure logging using a YAML file
* Use `logging.config.dictConfig()`
* Separate configuration from code

---

### 3. Code-Based Configuration

* Configure logging entirely in Python
* Define handlers, formatters, and loggers programmatically

---

### 4. FileHandler

* Write logs to a file
* Basic persistent logging setup

---

### 5. RotatingFileHandler

* Prevent large log files
* Automatically rotate logs based on size

---

### 6. Multiple Handlers

* Use multiple outputs simultaneously
* Example: console + file logging

---

### 7. Custom String Formatter

* Customize log message format
* Include timestamps, levels, and context

---

### 8. `extra` Parameter

* Add custom fields to log records
* Useful for structured and contextual logging

---

### 9. Custom Filters

* Filter logs using custom logic
* Control which logs are emitted

---

### 10. Custom Formatters

* Extend `logging.Formatter`
* Implement structured logging (e.g., JSON format)

---

### 11. Production Settings

* Suppress logging exceptions:

  ```python
  logging.raiseExceptions = False
  ```
* Ensure logging does not crash the application

---

## ⚠️ Best Practices

* Use log rotation in production
* Prefer structured (JSON) logging for scalability
* Keep logging configuration modular
* Avoid logging sensitive data

---

