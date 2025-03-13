# Uploading Files

<p id="terms"></p>

## Outline

-   Show how to upload files using [htmx][htmx]
-   File uploads require:
    1. HTML form with attribute `enctype="multipart/form-data"` to encode file data
    2. Server endpoint
    3. File storage
    4. Response handling to give user feedback.
-   htmx attributes used:
    -   `hx-encoding="multipart/form-data"` to encode file data
    -   `hx-post="/upload"` specifies upload endpoint
    -   `hx-target="#file-list"` specifies where to display the response
    -   `hx-swap="beforeend"` specifies how to insert response (append)
-   [`server.py`](./server.py`)
    -   Secures filenames to prevent path traversal attacks
    -   Limits maximum file size
    -   Provides endpoints for uploading, listing, and deleting files
    -   Serve static files from `../static` as before
-   Things we *should* do:
    -   Validate file types and content
    -   Virus/malware scanning
    -   Authentication and authorization for upload permissions

[htmx]: https://htmx.org/
