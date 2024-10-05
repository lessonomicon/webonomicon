# Using HTMX

-   Go back to the models, views, and server from [Serving HTML](../06_view/index.md)
    -   Strip out row and column views
    -   Add a button for each row
    -   Styling is ugly, so add a handler for static files in [`server.py`](./server.py) as well
-   Add an empty `div` with ID `experiments`
-   Add `htmx.js` to head of page to use [htmx][htmx]
-   Modify buttons to use it
    -   `hx-get`: get from URL
    -   `hx-trigger`: event that triggers action
    -   `hx-target`: ID of page element to modify in place
    -   `hx-swap`: replace inner HTML (as opposed to the entire element with `outerHTML`)
-   [htmx][htmx] searches document for properties starting `hx-` and adds appropriate callbacks

```
<button hx-get="/exp/{row.staff_id}" hx-trigger="click" hx-target="#experiments" hx-swap="innerHTML">
  x
</button>
```

-   Running it now produces 404 error
-   So implement `/exp/id` in server, models, and views
    -   `experiments` function in `models.py` uses an inner join
    -   Add `*args` to `handle_format` to [spread arguments](g:spread-arguments) for convenience
-   More common for server to return JSON that a JavaScript library in the browser translates into HTML
-   But that approach leads to large (slow) libraries in the browser
    -   Unfair to people using mobile, on slow connections, etc.

## Summary

[% figure
   id="htmx-concept-map"
   src="./htmx_concept_map.svg"
   alt="concept map of HTMX"
   caption="Concept Map"
%]

[htmx]: https://htmx.org/
