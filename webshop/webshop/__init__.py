from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.request import Response


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
