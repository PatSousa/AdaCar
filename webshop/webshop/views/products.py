import json
from pyramid.response import Response
from pyramid.view import (
    view_config,
    view_defaults
)

from sqlalchemy.exc import DBAPIError
from .default import db_err_msg

from ..models import PartType


@view_defaults(renderer='json')
class ProductViews:
    """Class that defines view to retrieve all orders"""
    def __init__(self, request):
        self.request = request

    @view_config(route_name='products_collections', renderer='json')
    def get_all_products(self):
        """Initial view to retrieve all products and render on page"""
        try:
            all_products = self.request.dbsession.query(PartType).order_by('part_type_category')
            all_products_serialized = [prod.to_json() for prod in all_products]
        except DBAPIError:
            return Response(db_err_msg, content_type='text/plain', status=500)
        resp = Response(json.dumps(all_products_serialized), content_type='json', charset='utf8')
        resp.headerlist.append(('Access-Control-Allow-Origin', '*')) # Add the access control
        return resp