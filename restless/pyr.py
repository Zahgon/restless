from pyramid.response import Response

from .constants import OK, NO_CONTENT
from .resources import Resource


class PyramidResource(Resource):
    """
    A Pyramid-specific ``Resource`` subclass.

    Doesn't require any special configuration, but helps when working in a
    Pyramid environment.
    """

    @classmethod
    def as_list(cls, *args, **kwargs):
        pass

    @classmethod
    def as_detail(cls, *init_args, **init_kwargs):
        pass

    def build_response(self, data, status=OK):
        pass

    @classmethod
    def build_routename(cls, name, routename_prefix=None):
        """
        Given a ``name`` & an optional ``routename_prefix``, this generates a
        name for a URL.

        :param name: The name for the URL (ex. 'detail')
        :type name: string

        :param routename_prefix: (Optional) A prefix for the URL's name (for
            resolving). The default is ``None``, which will autocreate a prefix
            based on the class name. Ex: ``BlogPostResource`` ->
            ``api_blogpost_list``
        :type routename_prefix: string

        :returns: The final name
        :rtype: string
        """
        pass

    @classmethod
    def add_views(cls, config, rule_prefix, routename_prefix=None):
        """
        A convenience method for registering the routes and views in pyramid.

        This automatically adds a list and detail endpoint to your routes.

        :param config: The pyramid ``Configurator`` object for your app.
        :type config: ``pyramid.config.Configurator``

        :param rule_prefix: The start of the URL to handle.
        :type rule_prefix: string

        :param routename_prefix: (Optional) A prefix for the route's name.
            The default is ``None``, which will autocreate a prefix based on the
            class name. Ex: ``PostResource`` -> ``api_post_list``
        :type routename_prefix: string

        :returns: ``pyramid.config.Configurator``
        """
        pass

