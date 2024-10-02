# Authentication

-   Assign everyone staff member a user ID and a 4-digit PIN
-   Encrypt the PINs
    -   For now use [reversible encryption](g:reversible-encryption)
    -   Most systems use one-way with a [salt](g:salt)
-   Generate account data with [`generate_accounts.py`](./generate_accounts.py)
    -   Use a [Jinja][jinja] template to produce a SQL file for migration
    -   Doesn't check for uniqueness of generated usernames
-   [`server.py`](./server.py)
    -   Set the user's staff ID as the cookie value (horribly insecure)
    -   Only show experiments to the person who created them
    -   Handling cookies in JavaScript (or Python) is unpleasant

[jinja]: https://jinja.palletsprojects.com/
