from typing import Optional

import dateparser as dateparser
import jsonpickle as jsonpickle
from datetime import datetime, date
from .constants import FORMATS


def flask_json_response(response, status_code=200) -> 'flask.Response':
    """
    pretty print to flask response as json
    """
    import flask

    return flask.Response(
        any2json(response, serialized=False) if response not in [None, '', {}] else None,
        content_type='application/json',
        status=status_code
    )


def any2json(value, serialized=True) -> str:
    """
    safe json parse.
    is necessary because mongoengine.Document isn't serializable
    """

    string_json = jsonpickle.encode(value, unpicklable=serialized)
    return string_json


def string2datetime(value: str) -> datetime:

    dmy = FORMATS.DATE.BR
    ymd = FORMATS.DATE.EN
    separators = ['', ' ', '-', '.', '/']
    date_formats = [f.format(sep=sep) for f in dmy + ymd for sep in separators]

    return dateparser.parse(value, date_formats=date_formats, languages=['pt', 'en'])

def datetime2json(value: (datetime, date)) -> Optional[str]:
    """
    force use only 1 date format like "YYYY-mm-dd HH:mm:ss"
    """
    if value is None:
        return None

    if not isinstance(value, (datetime, date)):
        raise ValueError(f'{value} isn\'t a valid datetime or date type')

    value = value.strftime('%Y-%m-%d %H:%M:%S')

    if '00:00:00' in value:
        value = value.split(' ')[0]

    return value
