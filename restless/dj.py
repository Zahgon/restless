import six

from django.conf import settings
from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .constants import OK, NO_CONTENT
from .exceptions import NotFound, BadRequest
from .resources import Resource


class DjangoResource(Resource):
    """
    A Django-specific ``Resource`` subclass.

    Doesn't require any special configuration, but helps when working in a
    Django environment.
    """

    def serialize_list(self, data):
        pass

    def wrap_list_response(self, data):
        pass

    # Because Django.
    @classmethod
    def as_list(self, *args, **kwargs):
        pass

    @classmethod
    def as_detail(self, *args, **kwargs):
        pass

    def is_debug(self):
        pass

    def build_response(self, data, status=OK):
        pass

    def build_error(self, err):
        pass

    @classmethod
    def build_url_name(cls, name, name_prefix=None):
        """
        Given a ``name`` & an optional ``name_prefix``, this generates a name
        for a URL.

        :param name: The name for the URL (ex. 'detail')
        :type name: string

        :param name_prefix: (Optional) A prefix for the URL's name (for
            resolving). The default is ``None``, which will autocreate a prefix
            based on the class name. Ex: ``BlogPostResource`` ->
            ``api_blog_post_list``
        :type name_prefix: string

        :returns: The final name
        :rtype: string
        """
        pass

    @classmethod
    def urls(cls, name_prefix=None):
        """
        A convenience method for hooking up the URLs.

        This automatically adds a list & a detail endpoint to your URLconf.

        :param name_prefix: (Optional) A prefix for the URL's name (for
            resolving). The default is ``None``, which will autocreate a prefix
            based on the class name. Ex: ``BlogPostResource`` ->
            ``api_blogpost_list``
        :type name_prefix: string

        :returns: A list of ``url`` objects for ``include(...)``
        """
        pass
