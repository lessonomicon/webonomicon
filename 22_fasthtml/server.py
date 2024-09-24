"""Serve data from data model layer with JWT authentication."""

from fasthtml.common import fast_app, serve, RedirectResponse
from starlette.requests import Request
from fasthtml.ft import Div, P

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
def root(request: Request):
    staff_id = None
    token = request.cookies.get(COOKIE_NAME)
    if token:
        staff_id = decode_token(token)
    return views.all_staff(models.all_staff(), staff_id)


@app.post("/login")
async def login_handler(request: Request):
    """Accept password and go back home."""
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    if not username or not password:
        response = RedirectResponse(url="/", status_code=303)
        response.delete_cookie(COOKIE_NAME)
        return response

    password = encrypt_password(secret, password)
    staff_id = models.authenticate(username, password)
    
    if staff_id is None:
        response = RedirectResponse(url="/", status_code=303)
        response.delete_cookie(COOKIE_NAME)
        return response

    token = create_token(staff_id)
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(COOKIE_NAME, token, httponly=True, samesite="Lax")
    return response


@app.get("/exp/{staff_id}")
async def exp(request: Request, staff_id: int):
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        return Div(P("Not authenticated. Please log in."))

    decoded_staff_id = decode_token(token)
    if decoded_staff_id is None:
        response = RedirectResponse(url="/", status_code=303)
        response.delete_cookie(COOKIE_NAME)
        return response

    if int(decoded_staff_id) == staff_id:
        experiments_data = models.experiments(staff_id)
        return views.experiments(experiments_data, staff_id)
    else:
        return Div(P("Not authorized to view this staff member's experiments."))


@app.get("/heartbeat")
def heartbeat():
    return views.heartbeat(HEARTBEAT)


serve(port=8000)
