"""Get data from database."""

import os
from pypika import Query, Table
import sqlite3

from util import ModelException, dict_factory


ENV_VAR = "DB"


class ModelException(Exception):
    """Problems with queries."""

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


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


def column(name):
    """Get a single column of staff."""
    staff = Table("staff")
    query = Query.from_(staff).select(name)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return [r[name] for r in cursor.fetchall()]
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))
    except KeyError as exc:
        raise ModelException(str(exc))


def row(staff_id):
    """Get a single row of staff."""
    staff = Table("staff")
    query = Query.from_(staff) \
                 .select("staff_id", "personal", "family") \
                 .where(staff.staff_id == staff_id)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        result = cursor.fetchall()
        if len(result) == 0:
            raise ModelException(f"no rows match {staff_id}")
        elif len(result) > 1:
            raise ModelException(f"multiple rows match {staff_id}")
        return result[0]
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))