# Using Forms

## Overview

[% figure
   id="forms-concept-map"
   src="./forms_concept_map.svg"
   alt="concept map of HTML forms"
   caption="Concept Map"
%]

<p id="terms"></p>

## Outline

-   Remove everything except display of a table of all staff
-   Add a [form](g:form) for adding new people
    -   Copy the database before running
-   [`explore_insert.py`](./explore_insert.py): experiment with insertion
    -   Select largest staff ID, add one, insert: race condition
    -   Better to build a subquery that does this
-   Add `add_staff` function to [`models.py`](./models.py)
    -   Must have `commit` in `models.add_staff`
    -   Really should check values…
