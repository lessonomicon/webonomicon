# Serving HTML

-   Introduce the view part of MVC and use [Jinja][jinja] templates
    -   Alternative [htpy][htpy] is more amenable to debugging but harder to read
-   Add exceptions to [`util.py`](./util.py)
    -   Common parent for all application exceptions to make catching easier
-   Load templates from filesystem in [`views.py`](./views.py)
    -   Allow caller to override default HTML template for `all_staff` for later use
-   Pass in data as named argument
-   Use the sample template for single-row and multi-row views
-   No changes to [`models.py`](./models.py)
-   A note on sub-directories:
    -   Most servers will not load things whose paths start with `../` for security reasons
    -   Run [`server_paths.py`](./server_paths.py) and go to `/dotdot` to see the effect
    -   So assets need to be in directories below the server's root directory
    -   But `../static/image.png` works because [Flask][flask] removes the leading `../`
-   The right way to do this is to configure a directory for [static files](g:static-file)
    -   [`server_static_paths.py`](./server_static_paths.py)
    -   `Flask("server", static_folder=Path("../img").absolute(), static_url_path="/static")`

## Summary

[% figure
   id="view-concept-map"
   src="./view_concept_map.svg"
   alt="concept map of views in MVC"
   caption="Concept Map"
%]

[flask]: https://flask.palletsprojects.com/
[htpy]: https://htpy.dev/
[jinja]: https://jinja.palletsprojects.com/
