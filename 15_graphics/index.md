# Dynamic Graphics

-   [SVG](g:svg) is a widely-used [vector graphics](g:vector-graphics) format
    -   Represent lines, circles, etc. in a notation like HTML
    -   Also represent transformations (move, rescale, etc.)
-   [`shapes.html`](./shapes.html) and [`shapes.js`](./shapes.js)
    -   Create an SVG object and insert into the page
    -   Ask that object to create other shapes
    -   Move them into position and change their properties
-   [`colors.js`](./colors.js) changes the color of a square dynamically
    -   Note the use of `window.addEventListener`
-   [`bar_chart.html`](./bar_chart.html): create a bar chart with fixed values
    -   A lot of calculations, many of which would have to be re-done if the X-axis labels weren't rotated
-   Use [Frappe Charts][frappe-charts]
    -   Not as popular as [Chart.js][chart-js], but it uses SVG

[chart-js]: https://www.chartjs.org/
[frappe-charts]: https://frappe.io/charts/docs
