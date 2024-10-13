# HTML and CSS

-   [HyperText Markup Language](g:html) (HTML) is the standard way to represent documents on the web
-   [Cascading Style Sheets](g:css) (CSS) is the standard way to style them
-   Both are more complicated than they should have been but we need to understand a bit of both

## HTML

-   HTML document contains [elements](g:element) and text
-   Elements are shown using [tags](g:tag)
    -   Opening tag `<tagname>` shows where the element begins
    -   Closing tag `</tagname>` shows where it ends
-   Elements must form a tree, i.e., must be strictly nested
    -   `<X>…<Y>…</Y></X>` is legal
    -   `<X>…<Y>…</X></Y>` is not
-   And every document should have a single [root element](g:root-element) that encloses everything else
-   Since `<` and `>` are used to show where tags start and end,
    must use [escape sequences](g:escape-sequence) to represent them
    -   Written `&name;`

[% table
   id="htmlcss-escape-characters"
   tbl="escape_characters.tbl"
   caption="Table 1: HTML Escape Characters"
%]

-   Well-formed HTML page has:
    -   `<!DOCTYPE html>` as the first line
    -   An `html` element enclosing everything else
    -   A single `head` element with metadata
    -   A single `body` element with content
-   Indentation doesn't matter to the browser (but make source more readable to people)
-   Use `<!--` and `-->` to start and end comments (which cannot be nested)

[% table
   id="htmlcss-html-tags"
   tbl="html_tags.tbl"
   caption="Table 2: HTML Tags"
%]

-   Customize elements with `name="value" [attributes](g:attribute)

```
<h1 align="center">A Centered Heading</h1>
```

-   Use `href` attribute of `a` element to link to:
    -   Another page with a full URL such as `https://example.com/page.html`
    -   A page relative to the current one such as `./examples/page.html`
    -   Another element in this page by ID such as `#main-title`

### UTF-8 Encoding

* UTF-8 Encoding (Simplified):
   - Think of UTF-8 as a universal language for computers to understand and display text.
   - It can handle almost any character from any language in the world, including emojis
   - When you use UTF-8, you don't have to worry about your text looking weird on different devices or websites.

* Specifying UTF-8 in HTML:
   - To ensure proper rendering of special characters, you should specify UTF-8 encoding in your HTML:
     ```
     <meta charset="utf-8">
     ```
   - This tag should be placed in the `<head>` section of your HTML document.

* HTML Entities vs. Direct Unicode Characters:
   - HTML entities like `&copy;` are useful for ensuring compatibility across different encodings and older systems.
   - With UTF-8 encoding (and the proper meta tag), you can directly use Unicode characters like © in your HTML.
   - Example:
     ```
     <p>&copy; 2024</p>
     <!-- is equivalent to -->
     <p>© 2024</p>
     ```
   - Both will render the same in a browser, but the direct Unicode character is more readable in the source code.

## CSS

-   `<h1 align="center" color="red">…</h1>` is frowned on these days
    -   Hard to keep styling consistent
-   Give elements [classes](g:css-class) and defines styles for classes
-   [`styled_page.html`](./styled_page.html) uses an [external style sheet](g:external-style-sheet)
    [`styled_page.css`](./styled_page.css)
    -   Which can be shared by many pages
-   Can define [CSS variables](g:css-variable) or style things directly
