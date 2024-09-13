# Contributing

Contributions are very welcome;
please contact us [by email][email] or by filing an issue in [our repository][repo].
All contributors must abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Setup and Operation

-   Install [uv][uv]
-   Create a virtual environment by running `uv venv` in the root directory
-   Activate it by running `source .venv/bin/activate` in your shell
-   Install dependencies by running `uv pip install -r pyproject.toml`
-   This project uses [mccole][mccole] to generate HTML and check the project's structure
-   Run `make` on its own to see a list of common commands

| make task | effect                                   |
| --------- | ---------------------------------------- |
| clean     | clean up                                 |
| commands  | show available commands (default)        |
| datasets  | re-create snailz parameters and datasets |
| lint      | check code and project                   |
| render    | convert to HTML                          |
| serve     | serve generated HTML                     |
| stats     | basic site statistics                    |

## Structure

-   Lessons are in `nn_slug` directories
    -   `nn` is two-digit sequence number
    -   `slug` is short mnemonic
-   Each lesson must have:
    -   `index.md`: lesson content
    -   `Makefile`: re-run tasks
        -   Should `include ../common.mk` to get common tasks
    -   Symbolic links `data`, `migrations`, and `static`
        to the `./data`, `./migrations`, and `./static` directories in the project root
    -   Lessons may have a `slides.md` file containing slides
    -   Diagrams should be SVG files created with [draw.io][draw-io]
-   `bibliography.md` has the bibliography as a definition list
    -   Citation keys have IDs for linking
    -   Use an inline HTML link `b:key` in files to create links
-   `glossary.md` has the glossary as definition list
    -   Reference keys have IDs for linking
    -   Use an inline HTML link `g:key` in files to create links
-   The `static` directory contains static files
    -   `page.css`: CSS for website pages
    -   `slides.css` and `slides.js`: simple HTML slides
    -   Other CSS and JavaScript files used in lessons
-   The `templates` directory contains [Jinja][jinja] templates used to generate HTML
    -   `page.html`: template for website pages
    -   `slides.html`: template for simple HTML slides

## Labels

| Name             | Description                  | Color   |
| ---------------- | ---------------------------- | ------- |
| change           | something different          | #FBCA04 |
| feature          | new feature                  | #B60205 |
| fix              | something broken             | #5319E7 |
| good first issue | newcomers are always welcome | #D4C5F9 |
| talk             | question or discussion       | #0E8A16 |
| task             | one-off task                 | #1D76DB |

Please use [Conventional Commits][conventional] style for pull requests
by using `change:`, `feature:`, `fix:`, or `task:` as the first word
in the title of the commit message.
You may also use `publish:` if the PR just rebuilds the HTML version of the lesson.

## FAQ

Do you need any help?
:   Yes—please see the issues in [our repository][repo].

What sort of feedback would be useful?
:   Everything is welcome,
    from pointing out mistakes in the code to suggestions for better explanations.

Can I add a new section?
:   Absolutely, but please [reach out][email] before doing so.

Why is this material free to read?
:   Because if we all give a little, we all get a lot.

## <a id="contributors">Contributors</a>

-   [*Juanan Pereira*][pereira-juanan] is a lecturer in Computer Science
    at the University of the Basque Country (UPV/EHU), where he researches and tries 
    to integrate open source software, software engineering, and LLMs in education.

-   [*Greg Wilson*][wilson-greg] is a programmer, author, and educator based in Toronto.
    He was the co-founder and first Executive Director of Software Carpentry
    and received ACM SIGSOFT's Influential Educator Award in 2020.

[draw-io]: https://www.drawio.com/
[email]: mailto:gvwilson@third-bit.com
[jinja]: https://jinja.palletsprojects.com/
[mccole]: https://github.com/gvwilson/mccole
[repo]: https://github.com/gvwilson/web-tutorial
[pereira-juanan]: https://ikasten.io/
[uv]: https://github.com/astral-sh/uv
[wilson-greg]: https://third-bit.com/
