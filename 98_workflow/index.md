# Designing a Workflow {: .fixme}

<p id="terms"></p>

## Examples

-   X is conducting a survey
    -   Site must be selected from pre-approved list (stored in database)
    -   Snail samples must be collected at predetermined grid points (hm… where are these?)
    -   GPS coordinates must be recorded for each sample (when are these checked and how do we tell if they're valid?)
    -   Each sample must have a unique identifier (does the collector generate this or does the system?)
    -   Snail size must be measured and recorded accurately (what are reasonable bounds for error checking?)
    -   Genetic material must be extracted and properly stored (how do we know?)
    -   Pollution levels must be measured at each grid point (as above…)
    -   All data must be recorded digitally in the field (realistically no way to enforce scientific honesty)
-   To implement survey data collection
    -   Create a `conduct_survey` page with a multi-step form
    -   Use GPS integration to automatically record coordinates
    -   Implement barcode scanning for sample identification
    -   Ensure offline functionality for field use
    -   Implement data validation before submission
-   To implement survey data upload
    -   Create an `upload_survey` page for batch data upload
    -   Check for data completeness and format consistency
    -   Validate sample IDs against existing database entries
    -   Ensure no duplicate entries are created
    -   Use transaction to ensure all-or-nothing data insertion
    -   Generate summary report after successful upload
-   To implement survey data quality control
    -   Add a `review_survey` page for supervisors
    -   Allow flagging of suspicious data points
    -   Implement a comment system for discussing data issues
    -   Require supervisor approval before data is marked as verified
    -   Log all changes and approvals for audit purposes
-   X is generating reports and visualizations
    -   User must have access to the data they want to report on
    -   Data must be filtered according to user-selected criteria (e.g., date range, site, pollution level)
    -   Reports should include summary statistics, graphs, and tables
    -   User must select export format (PDF, CSV, Excel)
    -   Data visualizations must be interactive and responsive
    -   Only authorized users can provide feedback on reports
-   To implement report and visualization creation
    -   Add a `create_report` page with data selection options
    -   Must handle user authentication and authorization checks
    -   Allow users to apply filters (e.g., date range, site, pollution level)
    -   Use a JavaScript library like Plotly for interactive visuals
    -   Implement responsive design for all visualizations
    -   Store user feedback in the database

## In Detail

-   Design plates for an experiment
    -   Sample must not already be claimed by an existing experiment
    -   Plates must parse correctly
    -   Plates cannot be duplicates
    -   One or more people must be associated with experiment
    -   Does the uploader have to be one of those people?
-   Invalidate a plate
    -   Person must have privileges
    -   A second person with privileges must OK the invalidation
    -   An example of work in progress
-   To implement experiment creation
    -   Add a `create_experiment` page with a form
    -   Must handle multiple file upload
    -   And check multiple people (no duplicates)
    -   No schema changes required
-   To implement plate invalidation
    -   Add a `confirmed_by` column to `invalidated`?
    -   But what if we decide two confirmations are needed? Or three?
    -   Would need a join table like `performed`
    -   Save that complexity until the day…
    -   For now just used `confirmed_by`
        -   Display confirmations with NULL as "awaiting"
