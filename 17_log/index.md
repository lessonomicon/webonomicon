# Logging and Auditing

<p id="terms"></p>

-   Add structured logging using [`structlog`][structlog]
-   Old-fashioned logging generates human-readable text:

```
2025-03-13 14:30:21 INFO: File 'example.txt' uploaded successfully
```

-   Structured logging writes data objects:

```json
{
  "timestamp": "2025-03-13T14:30:21.123Z",
  "level": "info",
  "event": "file_uploaded",
  "filename": "example.txt",
  "file_size_bytes": 12345,
  "content_type": "text/plain",
  "ip_address": "192.168.1.1",
  "user_agent": "Mozilla/5.0"
}
```

-   Benefits:
    -   Logs can be easily queried and analyzed by code (no fancy regular expressions)
    -   Every log event has the same fields
    -   More metadata can be included with each event
    -   Log entries can be rendered in different formats
-   Modify [`server.py`](./server.py)
    -   Logger configuration: set up `structlog` with appropriate processors
    -   Context binding: add context data to loggers
    -   Event-based logging: use specific event names rather than free-form messages
    -   Exception handling: capture structured exception information
    -   Standard fields: include common fields like timestamps
-   Specific enhancements
    -   Log all file operations (upload, delete, listing)
    -   Add request metadata (IP address, user agent)
    -   Include ile metadata (size, content type)
    -   Provide detailed error information
    -   Create a log viewer page
-   Best practices
    -   Log specific events rather than messages
    -   Use field names consistently
    -   Add relevant metadata to each log entry (e.g., timestamps)
    -   Never log sensitive data like passwords, tokens, or personal information
    -   Match log levels to the significance of events
-   Something we shouldn't have done
    -   Store all log messages in a global variable called `LOG` to display in the viewer page
-   In a production application we would:
    -   Configure `structlog` to output to a logging service or aggregator rather than just printing to the console
    -   Store logs in a database or dedicated log storage system rather than in memory
    -   Implement log rotation and retention policies
-   We create a new bound logger in each request handler rather than reusing a global bound logger because:
    -   Each HTTP request has unique context data (IP address, user agent, etc.) that should be captured in logs.
        Creating a fresh bound logger ensures each request gets its own context.
    -   Flask handles multiple requests concurrently,
        and reusing a global bound logger could lead to context data from one request leaking into logs for another request.
	(We actually run this example in single-threaded mode so that it's safe to append things to the `LOGS` variable,
	but as noted above,
	that's a bad practice.)
-   We use Flask's `before_request` handler to automatically log all incoming requests
    -   This ensures consistent handling and formatting of log events

```python
@app.before_request
def log_request():
    """Log all incoming requests."""
    if not request.path.startswith('/static'):
        logger.info("request", 
                  method=request.method,
                  path=request.path,
                  ip=request.remote_addr,
                  user_agent=request.headers.get('User-Agent'))
```

[structlog]: https://www.structlog.org/
