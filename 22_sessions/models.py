"""Get data from database."""

import os
from pypika import Query, Table
import sqlite3

from util import ModelException, dict_factory


ENV_VAR = "DATA"


def connect():
    """Connect to database."""
    path = os.getenv(ENV_VAR)
    if not path:
        raise ModelException(f"Environment variable {ENV_VAR} not set")
    connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = dict_factory
    return connection


def all_staff():
    """Get all staff."""
    staff = Table("staff")
    query = Query.from_(staff).select("staff_id", "personal", "family")
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def experiments(staff_id):
    """Get all experiments performed by staff member."""
    performed = Table("performed")
    experiment = Table("experiment")
    query = Query.from_(experiment)\
                 .inner_join(performed)\
                 .on(experiment.sample_id == performed.sample_id)\
                 .where(performed.staff_id == staff_id)\
                 .select(experiment.star)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def authenticate(username, password):
    """Try to authenticate, returning staff ID or None."""
    staff = Table("staff")
    query = Query.from_(staff)\
                 .select(staff.staff_id)\
                 .where((staff.username == username) & (staff.password == password))
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        result = cursor.fetchall()
        return result[0]["staff_id"] if (len(result) == 1) else None
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def create_session(cookie, staff_id):
    """Create a new session."""
    sessions = Table("sessions")
    query = Query.into(sessions).columns("cookie", "staff_id").insert(cookie, staff_id)
    try:
        connection = connect()
        connection.execute(str(query))
        connection.commit()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def get_session(cookie):
    """Get session by cookie."""
    sessions = Table("sessions")
    query = Query.from_(sessions).select("staff_id").where(sessions.cookie == cookie)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        result = cursor.fetchone()
        return result["staff_id"] if result else None
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def delete_session(cookie):
    """Delete a session."""
    sessions = Table("sessions")
    query = Query.from_(sessions).delete().where(sessions.cookie == cookie)
    try:
        connection = connect()
        connection.execute(str(query))
        connection.commit()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))