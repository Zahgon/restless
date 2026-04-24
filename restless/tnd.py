from tornado import web, gen
from .constants import OK, NO_CONTENT
from .resources import Resource
from .exceptions import MethodNotImplemented, Unauthorized

import weakref
import inspect


try:
    from tornado.concurrent import is_future
except ImportError:
    is_future = None

if is_future is None:
    """
    Please refer to tornado.concurrent module(newer than 4.0)
    for implementation of this function.
    """
    try:
        from concurrent import futures
    except ImportError:
        futures = None

    from tornado.concurrent import Future

    if futures is None:
        FUTURES = Future
    else:
        FUTURES = (Future, futures.Future)

    is_future = lambda x: isinstance(x, FUTURES)


@gen.coroutine
def _method(self, *args, **kwargs):
    """
    the body of those http-methods used in tornado.web.RequestHandler
    """
    pass


class _BridgeMixin(object):
    """
    This mixin would pass tornado parameters to restless,
    and helps to init a resource instance
    """
    def __init__(self, *args, **kwargs):
        pass


class TornadoResource(Resource):
    """
    A Tornado-specific ``Resource`` subclass.
    """

    _request_handler_base_ = web.RequestHandler
    """
    To override ``tornado.web.RequestHandler`` we used,
    please assign your RequestHandler via this attribute.
    """

    def __init__(self, *args, **kwargs):
        pass

    @property
    def r_handler(self):
        """
        access to ``tornado.web.RequestHandler``
        """
        pass

    @classmethod
    def as_view(cls, view_type, *init_args, **init_kwargs):
        """
        Return a subclass of tornado.web.RequestHandler and
        apply required setting.
        """
        pass

    def request_method(self):
        pass

    def request_body(self):
        pass

    def build_response(self, data, status=OK):
        pass

    def is_debug(self):
        pass

    @gen.coroutine
    def handle(self, endpoint, *args, **kwargs):
        """
        almost identical to Resource.handle, except
        the way we handle the return value of view_method.
        """
        pass


