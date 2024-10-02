# Permissions

-   Everyone can read everything
    -   Databases like [PostgreSQL][postgresql] implement fine-grained permissions on tables and even rows
    -   But we need to do it ourself for [SQLite][sqlite]
    -   Note that if someone has access to the `.db` file, we have no protection
-   If we're going to add create, update, and delete, we should add *permissions*
    -   The ability to perform an operation on a thing
-   Standard approach:
    -   An [actor](g:actor) (person or similar) has zero or more [roles](g:role)
    -   Each role is a set of [permissions](g:permission)
    -   E.g., *reader* role has *read* permission for all tables
-   Represent permissions with two tables in the database
    -   Worry about authentication later
-   Add two new tables
    -   `role` is a many-to-many join table
    -   `permission` defines what roles mean (with wildcard for "all tables")
    -   Put these in a temporary copy of the database for now
-   Could write a `require` function to check permission before doing database query
    -   But what if someone modifies the database between our check and the main query?
-   Use `join` to only select rows where permission is available
    -   But this means we can't distinguish "no data" from "no permission"
-   [`explore_permissions.py`](./explore_permissions.py) explores ways to do what we want with [PyPika][pypika]
    -   Turns out that `join` must have `on`
    -   Since we want everything, use `x == x`
-   Having explored ideas in the small, we can implement in the large
    -   [`test_json.py`](./test_json.py) uses a custom [PyPika][pypika] function to call SQLite's `json_group_array`
    -   Name the JSON field `something__json`
    -   Modify `dict_factory` to unpack and rename
-   Go back to [`test_permissions.py`](./test_permissions.py) and add tests using this
    -   Hard to understand without building it up in steps, but it works

[postgresql]: https://www.postgresql.org/
[pypika]: https://pypika.readthedocs.io/
[sqlite]: https://www.sqlite.org/
