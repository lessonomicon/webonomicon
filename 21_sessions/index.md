# Sessions

-   Sessions are forgotten when the server restarts
    -  But cookie persists, which is confusing
    - [`server_sessions.py`](./server_sessions.py) stores  sessions in SQLite
-   Store the user's session ID in the database
    -  When the user logs in, create a new session and store the session ID as a cookie
    -  When the user makes a request, check if the session ID in the cookie matches the session ID in the database
- Implement session-based authentication using SQLite
    -  Create a `sessions` table in the database to store session IDs and corresponding user IDs
    - `create_session`, `get_session`, and `delete_session` functions are implemented in [`models.py`](./models.py)
- JSON Web Tokens [JWT][jwt] could be used as an alternative to session-based authentication
    - Lightweight JSON-based authentication mechanism
    - Encode and sign user claims as JSON
    - Client stores the resulting token
    - [jwt.io][jwt-io] allows you to decode, verify and generate JWT.
    
[jwt]: https://en.wikipedia.org/wiki/JSON_Web_Token
[jwt-io]: https://jwt.io
