from flask import make_response
from flask import request

from .constants import OK, NO_CONTENT
from .resources import Resource


class FlaskResource(Resource):
    """
    A Flask-specific ``Resource`` subclass.

    Doesn't require any special configuration, but helps when working in a
    Flask environment.
    """
    @classmethod
    def as_list(cls, *init_args, **init_kwargs):
        # Overridden here, because Flask uses a global ``request`` object
        # rather than passing it to each view.
        def _wrapper(*args, **kwargs):
            # Make a new instance so that no state potentially leaks between
            # instances.
            pass

        return _wrapper

    @classmethod
    def as_detail(cls, *init_args, **init_kwargs):
        # Overridden here, because Flask uses a global ``request`` object
        # rather than passing it to each view.
        def _wrapper(*args, **kwargs):
            # Make a new instance so that no state potentially leaks between
            # instances.
            pass

        return _wrapper

    def request_body(self):
        return self.request.data

    def is_debug(self):
        from flask import current_app
        return current_app.debug

    def build_response(self, data, status=OK):
        if status == NO_CONTENT:
            # Avoid crashing the client when it tries to parse nonexisting JSON.
            content_type = 'text/plain'
        else:
            content_type = 'application/json'
        return make_response(data, status, {
            'Content-Type': content_type,
        })

    @classmethod
    def build_endpoint_name(cls, name, endpoint_prefix=None):
        """
        Given a ``name`` & an optional ``endpoint_prefix``, this generates a name
        for a URL.

        :param name: The name for the URL (ex. 'detail')
        :type name: string

        :param endpoint_prefix: (Optional) A prefix for the URL's name (for
            resolving). The default is ``None``, which will autocreate a prefix
            based on the class name. Ex: ``BlogPostResource`` ->
            ``api_blogpost_list``
        :type endpoint_prefix: string

        :returns: The final name
        :rtype: string
        """
        pass

    @classmethod
    def add_url_rules(cls, app, rule_prefix, endpoint_prefix=None):
        """
        A convenience method for hooking up the URLs.

        This automatically adds a list & a detail endpoint to your routes.

        :param app: The ``Flask`` object for your app.
        :type app: ``flask.Flask``

        :param rule_prefix: The start of the URL to handle.
        :type rule_prefix: string

        :param endpoint_prefix: (Optional) A prefix for the URL's name (for
            endpoints). The default is ``None``, which will autocreate a prefix
            based on the class name. Ex: ``BlogPostResource`` ->
            ``api_blog_post_list``
        :type endpoint_prefix: string

        :returns: Nothing
        """
        pass
