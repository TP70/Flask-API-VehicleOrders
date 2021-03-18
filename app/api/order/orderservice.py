import logging

from bson.errors import InvalidId

from app.domain.order import Order
from app.domain.order_repository import OrderRepository
from bson.objectid import ObjectId

log = logging.getLogger(__name__)


class OrderService(object):
    def __init__(self):
        self.repository = OrderRepository()

    # returns the order id
    def create_order(self, data):
        return self.repository.create(Order.build_and_validate(data))

    def get_order(self, order_id):
        try:
            ObjectId(order_id)
        except InvalidId:
            msg = f"Not a valid order id: {order_id}"
            log.exception(msg)
            raise Exception(msg)
        else:
            return self.repository.read(order_id)

    def update_order(self, order_id, order):
        try:
            order["_id"] = ObjectId(order_id)
        except Exception as e:
            log.warning(
                "Attempt to update order with invalid id: ",
                e.__class__,
                ", creating new entry instead",
            )
        finally:
            return self.repository.update(Order.build_and_validate(order))
