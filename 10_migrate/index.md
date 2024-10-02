# Database Migration

-   A [database migration](g:db-migration) is a change to the structure of a database
    -   Versus a change to its contents
-   Use tools like [sqitch][sqitch] to manage these
-   Each change has three parts
    -   Forward: make the desired change
    -   Check: make sure it happened
    -   Backward: undo it (after checking that it was done)
-   [`migrate.py`](./migrate.py) looks for files with structured names
    -   Forward: `NN_fwd_mnemonic.sql` (`NN` is sequence number, `mnemonic` is long meaningful name)
    -   Check: `NN_check_mnemonic.sql`
    -   Backward: `NN_bwd_mnemonic.sql`
-   Example
    -   [`../migrations/01_fwd_add_roles_permissions.sql`](../migrations/01_fwd_add_roles_permissions.sql)
    -   [`../migrations/01_check_add_roles_permissions.sql`](../migrations/01_check_add_roles_permissions.sql)
    -   [`../migrations/01_bwd_add_roles_permissions.sql`](../migrations/01_bwd_add_roles_permissions.sql)
-   Keep these files in version control

[sqitch]: https://sqitch.org/
