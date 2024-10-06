# Logging and Auditing

- Introduction to logging and auditing
  - Importance in web applications
  - Difference between logging and auditing

- Logging
  - Purpose: debugging, monitoring, error tracking
  - Python's built-in logging module
  - Configuring log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Creating log handlers (console, file)
  - Formatting log messages
  - Python logging frameworks (Maybe loguru? https://github.com/Delgan/loguru)
  
- Implementing logging in our application
  - Adding logging to server.py
  - Logging database operations in models.py
  - Logging user actions in views.py

- Auditing
  - Purpose: security, compliance, user activity tracking
  - Difference from general logging
  - What to audit: user logins, data access, changes to data

- Implementing auditing in our application
  - Creating an audit table in the database
  - Adding audit entries for:
    - User authentication attempts
    - Data access (e.g., viewing experimental data)
    - Data modifications (e.g., adding new experiments)

- Challenges and considerations
  - Performance impact of extensive logging/auditing
  - Storage requirements for logs and audit trails
  - Log rotation and retention policies
  - Avoiding sensitive data in logs