"""Serve data from data model layer with JWT authentication."""

from fasthtml.common import cookie, fast_app, serve
from fasthtml.ft import Titled
import jwt
from datetime import datetime, timedelta, timezone
import os

import models
import views
from util import encrypt_password, get_secret


COOKIE_NAME = "webonomicon"
HEARTBEAT = {"message": "alive"}
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_DELTA = timedelta(hours=1)


def create_token(staff_id):
    payload = {
        "exp": datetime.now(timezone.utc) + JWT_EXPIRATION_DELTA,
        "iat": datetime.now(timezone.utc),
        "staffId": staff_id
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["staffId"]
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token


app, rt = fast_app(
    pico=False,
    static_path="../static",
)
secret = get_secret()


@app.get("/")
def root():
    return views.all_staff(models.all_staff())


@app.post("/login")
def login_handler():
    """Accept password and go back home."""
    username = request.form["username"]
    password = request.form["password"]
    response = make_response(redirect(url_for("root")))

    if (not username) or (not password):
        response.set_cookie(COOKIE_NAME, "", expires=0)
        return response

    password = encrypt_password(secret, password)
    staff_id = models.authenticate(username, password)
    if staff_id is None:
        response.set_cookie(COOKIE_NAME, "", expires=0)
        return response

    token = create_token(staff_id)
    response.set_cookie(COOKIE_NAME, token, samesite="Lax")
    return response


@app.get("/exp/{staff_id}")
def exp(staff_id):
    staff_id = int(staff_id)
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        return Titled("Not authenticated")

    decoded_staff_id = decode_token(token)
    if decoded_staff_id is None:
        return Titled("Invalid or expired token")

    if int(decoded_staff_id) == staff_id:
        return views.experiments(models.experiments(staff_id), staff_id)
    else:
        return Titled("Not authorized")


@app.get("/heartbeat")
def heartbeat():
    return views.heartbeat(HEARTBEAT)


serve(port=8000)
