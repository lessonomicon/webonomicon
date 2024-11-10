# FastHTML

<p id="terms"></p>

-   [FastHTML][fasthtml] is a web application framework
    -   A single install to get everything we've built in pieces
-   Recycle our existing [`models.py`](./models.py)
-   [`server.py`](./server.py) looks pretty much the same
    -   Use `fast_app()` to create the application
    -   Define a static file directory when we do so
-   Biggest change is [`views.py`](./views.py)
    -   Create HTML with nested function calls instead of [Jinja][jinja] templates
-   Resulting application doesn't differ much from what we had
    -   Might have been easier to build if we'd started with [FastHTML][fasthtml]
    -   HTML-as-functions might feel more natural if we had used that first
    -   On balance, doesn't feel worth switching (yet)

[fasthtml]: https://docs.fastht.ml/
[jinja]: https://jinja.palletsprojects.com/
