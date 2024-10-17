# Internationalization

-   [Internationalization](g:i18n) (often abbreviated "i18n" because of the number of letters)
    is the preparation of software for multilingual support
-   [Localization](g:l10n) (often abbreviated "l10n") is the process of making internationalized software accessible
    to people using various languages and symbologies
-   A lot of software is built on top of [gettext][gettext]
-   We will build our own to show how it works
-   [`test_translation.py`](./test_translation.py):
    -   Register a function with [Jinja2][jinja] so that we can call it inside our template
    -   Define a translation table
    -   Use an object that creates a translation function that captures the language
    -   Call the translation function `_()` to save typing
-   [`util.py`](./util.py) loads a translation table based on (yet another) environment variable
-   [`views.py`](./views.py) uses the request's `accept_languages` property to look up the user's desired language code
-   [`server.py`](./server.py) passes `request.accept_languages` to view functions
-   [`request_lang.py`](./request_lang.py) gets a resource with an explicit `Accept-Language` header
    -   Can/should use unit tests from [Testing the Server](../08_test/index.md)
        and [Testing in the Browser](../14_automate/index.md)

[gettext]: https://en.wikipedia.org/wiki/Gettext
[jinja]: https://jinja.palletsprojects.com/
