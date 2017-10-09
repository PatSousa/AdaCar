from __future__ import absolute_import

from dateutil import parser
import json

from pyramid.view import (
    view_config,
    view_defaults
)
from pyramid.response import Response

from ..models import Order, Part


@view_defaults(renderer='json')
class OrderViews:
    """
    Class defining views for the order handling
    """
    def __init__(self, request):
        self.request = request
        self.DBsession = self.request.dbsession

    @view_config(route_name='orders_collections', renderer='json', request_method='POST')
    def create_order(self):
        """View to create order. POST with the type part being added."""
        data = self.request.json_body

        parts = self.DBsession.query(Part).filter_by(
            part_type=data.get('part_type_id'),
            order=None)

        order = Order()
        self.DBsession.add(order)
        self.DBsession.flush()

        for part in parts:
            part.order = order.order_id
            self.DBsession.add(part)
            self.DBsession.flush()

        resp = Response(json.dumps({'order_id':order.order_id}), content_type='json', charset='utf8')
        resp.headerlist.append(('Access-Control-Allow-Origin', '*'))

        return resp

    @view_config(route_name='orders_collections', renderer='json', request_method='GET')
    def get_all_orders(self):
        """View to get all orders. Not being currently used"""
        orders = self.DBsession.query(Order).all()
        serialized_orders = [order.to_json() for order in orders]
        return json.dumps({'orders': serialized_orders})

    @view_config(route_name='orders', renderer='json', request_method='POST')
    def update_order(self):
        """
        view to update the order. Should be a PUT according to REST verbs.
        If only part is given it updates part. If date is in the request body, updates date time.
        """
        order_id = int(self.request.matchdict['order_id'])
        order = self.DBsession.query(Order).filter_by(order_id=order_id).first()
        data = self.request.json_body

        parts = self.DBsession.query(Part).filter_by(
            part_type=data.get('part_type_id'),
            order=None)

        if order:
            for part in parts:
                part.order = order.order_id
                self.DBsession.add(part)
                self.DBsession.flush()

        if data.get('delivery_date'):
            order_delivery = parser.parse(data.get('delivery_date'))
            order.delivery_date = order_delivery
            self.DBsession.add(order)
            self.DBsession.flush()

        resp = Response(json.dumps({'order_id':order.order_id}), content_type='json', charset='utf8')
        resp.headerlist.append(('Access-Control-Allow-Origin', '*'))
        return resp

    @view_config(route_name='orders', renderer='json', request_method='GET')
    def get_order(self):
        """"Get a certain order"""
        order_id =  int(self.request.matchdict['order_id'])
        order = self.DBsession.query(Order).filter_by(order_id=order_id).first()
        return order.to_json()

    # @view_config(route_name='orders', renderer='json', request_method='DELETE')
    # def delete_order(self):
    #     """
    #     view to delete the order.
    #     """
    #     order_id = self.request.matchdict['order_id']

    #     order = self.request.dbsession.query(Order).filter_by(order_id=order_id).first()

    #     if order:
    #         # Get order parts - could (should) be done on model
    #         parts = self.request.dbsession.query(Part).filter_by(order=order_id)
    #         if parts.count() and not isinstance(parts, list):
    #             parts = [parts]
    #         for part in parts:
    #             part.order = None
    #             self.DBsession.add(part)
    #             self.DBsession.flush()

    #         self.request.dbsession.delete(order)
    #         self.DBsession.flush()
    #         return {'deleted': 'true'}
    #     else:
    #         return {'deleted': 'false'}

