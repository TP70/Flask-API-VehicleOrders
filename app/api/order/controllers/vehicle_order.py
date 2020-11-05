import logging

from flask_restplus import Resource
from flask import request

from app.api.order.orderservice import OrderService
from app.api.order.serializers import order, save_order
from app.api.restconfig import api

log = logging.getLogger(__name__)

ns = api.namespace("vehicle/order", description="Operations related to vehicle Orders")

order_service = OrderService()


@ns.route("/")
class OrderCollection(Resource):

    # list of orders
    # @api.marshal_list_with(order)
    # def get(self):
    #     orders = Order.get
    #     return orders

    @api.response(201, "Order successfully created.")
    @api.expect(save_order)
    def post(self):
        data = request.json
        return str(order_service.create_order(data)), 201


@ns.route("/<string:id>")
@ns.param("id", "The order identifier")
class Order(Resource):
    @api.response(404, "Order not found.")
    @api.response(200, "Order found.")
    @api.marshal_with(order)
    def get(self, id):
        try:
            return order_service.get_order(id)
        except Exception as e:
            ns.abort(404, status=repr(e), statusCode="404")

    @api.expect(save_order)
    @api.response(204, "Order successfully updated.")
    def put(self, id):
        data = request.json
        return str(order_service.update_order(id, data)), 204
