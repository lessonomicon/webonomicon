# A Graphical User Interface

-   Use [Alpine][alpine] to make a graphical editor for plate layouts
    -   What treatment is applied to each cell
    -   Personal details
-   Use CSS [flexbox](g:flexbox) layout to create two-column page
-   [`handwritten.html`](./handwritten.html) creates everything manually
-   Shared data stored in `x-data` attribute of enclosing `div` (the row)
    -   `treatments` is available treatments (including emptry string for "none")
    -   `current` is currently-selected treatment
    -   `data` is the plate data keyed by row/column identifier
-   Selectors are [radio buttons](g:radio-button)
    -   Share the same name to make them a group (only one can be selected at a time)
    -   Value is self-explanatory
    -   `x-model` property tells [Alpine][alpine] what to assign the value to
    -   Writing these by hand was annoying
-   Plate is a table
    -   Each cell's `x-text` property tells [Alpine][alpine] where to get data to display
    -   `x-on:click` is the action to take when the cell is clicked
-   Note: do *not* change cell values directly
    -   MVC: controller updates the model, view reflects the model
-   Templating
    -   Template in [`templates/design_simple.html`](./templates/design_simple.html)
    -   For now, use [`render.py`](./render.py) to test it out
    -   Templated version is 51 lines instead of 72, but will automatically expand as we go to larger plates
-   Now add dosages in [`templates/design_dosages.html`](./templates/design_dosages.html)
    -   Invariant: (no treatment and no dosage) or (some treatment and some dosage)
    -   I.e., cannot have a treatment with no dosage, and cannot have a dosage if no treatment selected
    -   Initialize to "no treatment" (empty string) and "no dosage" (also empty string)
        -   But no radio button for "no dosage" case
    -   When a treatment is first selected, the dosage is set to the minimum dosage
    -   Use `$watch` to watch for changes to the `current_treatment` and `current_dosage` variables
    -   Update the other state elements accordingly
    -   Again, the controller updates the model, the view displays its current state

[alpine]: https://alpinejs.dev/
