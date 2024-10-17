# Using a Database

## Overview

<figure id="db-concept-map">
  <img src="db_concept_map.svg" alt="concept map of database interaction in Python"/>
  <figcaption>Figure 1: Concept Map</figcaption>
</figure>

<p id="terms"></p>

## Outline

### Direct SQL

-   Use [SQLite][sqlite] database in `./data/lab.db` instead of CSV file
-   Install `_dict_factory` [factory function](g:factory-function)
    to get results as list of dictionaries instead of list of tuples
-   And use a flag to convert types like dates and times (used later)
-   [`models_sql.py`](./models_sql.py) implements model part of model-view-controller (MVC)
    -   One function for each question we might ask of our data
    -   Use SQL directly instead of an [object-relational mapper](g:orm)
        like [SQLAlchemy][SQLAlchemy], [SQLModel][sqlmodel], or [Pony][pony]
    -   ORMs can be hard to debug and don't perfectly insulate programs from changes to [schema](g:db-schema)

<pre data-file="models_sql.py"></pre>

-   Re-create connection each time model is accessed
    -   Creating it once and attaching to the [Flask][flask] app fails because of [multithreading](g:multithreading)
-   Catch SQLite exceptions and raise our own so that our server only has to catch one thing
-   Add some more error handling

### Query Builder

-   Security problem: we're inserting a user-defined name into a query
    -   Can't parameterize query on column name
    -   Opens us up to SQL injection attack
-   And embedded SQL isn't actually that easy to read
-   Use the [PyPika][pypika] [query builder](g:query-builder)
-   [`pika_demo.py`](./pika_demo.py) is a proof of concept

<pre data-file="pika_demo.py"></pre>

-   [`models_pika.py`](./models_pika.py) is shorter and more readable than the SQL version

<pre data-file="models_pika.py"></pre>

[flask]: https://flask.palletsprojects.com/
[pony]: https://ponyorm.org/
[pypika]: https://pypika.readthedocs.io/
[SQLAlchemy]: https://www.sqlalchemy.org/
[sqlite]: https://www.sqlite.org/
[sqlmodel]: https://sqlmodel.tiangolo.com/
