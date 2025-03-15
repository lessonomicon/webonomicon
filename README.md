# The Webonomicon

<p class="subtitle">An Introduction to Web Programming for the Cautious and Weary</p>

<div class="row" markdown="1">
  <div class="col-4 center">
    <img src="./static/advent_05_354.png" alt="Advent 354 by Danielle Navarro" style="width: 80%">
  </div>
  <div class="col-8" markdown="1">

This tutorial is a short introduction to web programming using modern tools and practices
for data scientists who are comfortable using Python
but have never built interactive websites before.
All of the material is available under [open licenses](./LICENSE.md),
and contributions through our [GitHub repository][repo] are welcome.
All contributors are required to respect our [Code of Conduct](./CODE_OF_CONDUCT.md).

> **Please note:** this tutorial is still being outlined.
> Most sections will have additional examples (and much more explanation)
> before learners encounter it.
> Suggestions and help are greatly appreciated.

  </div>

</div>

## Learner Persona

-   Sabina, 28, has a master's degree in animal physiology
    and now works for a mid-sized veterinary pharmaceutical company.
-   She learned a bit of R in an undergraduate biostatistics course,
    then picked up Python in grad school.
    She spends several hours a week analyzing data with [Pandas][pandas]
    and visualizing it with [Plotly Express][plotly-express],
    and is comfortable with basic Git commands.
-   Sabina recently became responsible for maintaining a dashboard application built with [Dash][dash].
    She believes a better understanding of how web applications work in general
    will help her debug and extend it.
-   Sabina has tried doing asynchronous online courses a couple of times,
    but strongly prefers learning in real time with other people.

## Syllabus

<div class="chapters" markdown="1">

1.  [Introduction](./01_intro/index.md): what we will learn, how to set up, and the data we will use
1.  [HTML and CSS](./02_htmlcss/index.md)
1.  [An Hour of JavaScript](./03_js/index.md)
1.  [JavaScript in the Browser](./04_browser/index.md): using the language in its native habitat
1.  [HTTP](./05_http/index.md): how browsers and server talk to each other
1.  [A Server](./06_server/index.md): building a server with [Flask][flask]
1.  [Using a Database](./07_db/index.md): getting data from [SQLite][sqlite] using [PyPika][pypika]
1.  [Testing the Server](./08_test/index.md): testing the server with [pytest][pytest]
1.  [Serving HTML](./09_view/index.md): generating HTML with [Jinja][jinja] templates
1.  [Using Forms](./10_forms/index.md): sending data to a server
1.  [Using HTMX](./11_htmx/index.md): letting the [htmx][htmx] library do the hard work
1.  [Database Migration](./12_migrate/index.md): managing database schema changes
1.  [Authentication](./13_auth/index.md): checking the user's identity
1.  [Testing in the Browser](./14_automate/index.md): using [Selenium][selenium] to test the user interface
1.  [Encryption](./15_crypt/index.md): keeping secrets safe
1.  [Uploading Files](./16_upload/index.md): multi-step interactions
1.  [Logging and Auditing](./17_log/index.md): keeping of track of what's happened
1.  [Permissions](./18_perm/index.md): representing and checking who can do what
1.  [Accessibility](./19_access/index.md): because everyone should be comfortable
1.  [A Graphical User Interface](./20_gui/index.md): handling interactivity in the browser
1.  [Dynamic Graphics](./21_graphics/index.md): drawing pictures with [SVG.js][svgjs]
1.  [Internationalization](./22_intl/index.md): because everyone should be welcome
1.  [Sessions](./23_sessions/index.md): persistent sessions and [JWT][jwt]
1.  [Caching](./24_cache/index.md): speeding things up

</div>

##  Appendices

<div class="appendices" markdown="1">

1.  [Designing a Workflow](./98_workflow/index.md)
1.  [Certificates](./99_cert/index.md)
1.  [License](./LICENSE.md)
1.  [Code of Conduct](./CODE_OF_CONDUCT.md)
1.  [Contributing](./CONTRIBUTING.md)
1.  [Bibliography](./bibliography.md)
1.  [Glossary](./glossary.md)

</div>

## Technologies

| Package                          | Purpose           |
| -------------------------------- | ----------------- |
| [Alpine.js][alpine]              | dynamic HTML      |
| [Beautiful Soup][bs4]            | HTML manipulation |
| [deno][deno]                     | JavaScript        |
| [FastHTML][fasthtml]             | web framework     |
| [Flask][flask]                   | web server        |
| [Frappe Charts][frappe-charts]   | charts            |
| [html5validator][html5validator] | validation        |
| [htmx][htmx]                     | interaction       |
| [httpx][httpx]                   | HTTP              |
| [Jinja2][jinja]                  | HTML templating   |
| [Polars][polars]                 | tabular data      |
| [PrettyTable][prettytable]       | formatting        |
| [PyPika][pypika]                 | query builder     |
| [pytest][pytest]                 | testing           |
| [Selenium][selenium]             | testing           |
| [SQLite][sqlite]                 | database          |
| [SVG.js][svgjs]                  | graphics          |

[alpine]: https://alpinejs.dev/
[bs4]: https://beautiful-soup-4.readthedocs.io/
[dash]: https://dash.plotly.com/
[deno]: https://deno.com/
[fasthtml]: https://docs.fastht.ml/
[flask]: https://flask.palletsprojects.com/
[frappe-charts]: https://frappe.io/charts/docs
[html5validator]: https://pypi.org/project/html5validator/
[htmx]: https://htmx.org/
[httpx]: https://www.python-httpx.org/
[jinja]: https://jinja.palletsprojects.com/
[jwt]: https://en.wikipedia.org/wiki/JSON_Web_Token
[pandas]: https://pandas.pydata.org/
[plotly-express]: https://plotly.com/python/plotly-express/
[polars]: https://pola.rs/
[prettytable]: https://pypi.org/project/prettytable/
[pypika]: https://pypika.readthedocs.io/
[pytest]: https://docs.pytest.org/
[repo]: https://github.com/lessonomicon/webonomicon
[selenium]: https://pypi.org/project/selenium/
[sqlite]: https://www.sqlite.org/
[svgjs]: https://svgjs.dev/
