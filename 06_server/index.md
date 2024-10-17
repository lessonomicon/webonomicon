# A Server

## Overview

<figure id="server-concept-map">
  <img src="server_concept_map.svg" alt="concept map of Flask server"/>
  <figcaption>Figure 1: Concept Map</figcaption>
</figure>

<p id="terms"></p>

## Outline

-   [`server_hello.py`](./server_hello.py): return HTML

<pre data-file="server_hello.py"></pre>

-   Go to http://127.0.0.1:5000 to view (5000 being [Flask][flask]'s default port)
    -   Or use [`fetch.py`](./fetch.py) to fetch and display data

<pre data-file="fetch.py"></pre>

-   [`server_func.py`](./server_func.py) creates the application and configures [routes](g:route) in a function
    -   Get path to staff CSV from `DATA` [environment variable](g:env-var)
    -   Read and convert to HTML with [PrettyTable][prettytable]

<pre data-file="server_func.py" data-keep="create"></pre>

-   [`server_routes.py`](./server_routes.py) configures several routes
    -   Use [query parameters](g:query-parameter) or [URL fragments](g:url-fragment)
        to select individual row or column
    -   Use [Polars][polars] to get a [dataframe](g:dataframe) and [Flask][flask] to convert to JSON

<pre data-file="server_routes.py" data-keep="create"></pre>

-   Some endpoints return HTML, some return JSON
    -   No endpoint should return both
-   [`server_err.py`](./server_err.py) handles errors
    -   Check row and column and raise exception if not there
    -   Rely on [Flask][flask] to handle nonexistent routes

<pre data-file="server_err.py" data-keep="create"></pre>

[flask]: https://flask.palletsprojects.com/
[polars]: https://pola.rs/
[prettytable]: https://pypi.org/project/prettytable/