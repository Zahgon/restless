
import datetime
import decimal
import json
import traceback
import uuid


class MoreTypesJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that allows for more common Python data types.

    In addition to the defaults handled by ``json``, this also supports:

        * ``datetime.datetime``
        * ``datetime.date``
        * ``datetime.time``
        * ``decimal.Decimal``
        * ``uuid.UUID``

    """
    def default(self, data):
        pass


def format_traceback(exc_info):
    pass
