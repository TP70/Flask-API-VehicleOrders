import pymongo

from app import settings
from bson.objectid import ObjectId


class OrderRepository(object):
    def __init__(self):
        # initializing the MongoClient, this helps to
        # access the MongoDB databases and collections
        self.client = pymongo.MongoClient(
            host=settings.MONGODB_HOST,
            username=settings.MONGODB_USER,
            password=settings.MONGODB_PASS,
            serverSelectionTimeoutMS=settings.MONGODB_TIMEOUT,
            connect=True,
        )

        self.db = self.client[settings.MONGODB_DB]
        self.orders = self.db["orders"]

    def create(self, order):
        """
        Method used to create a new entry
        """
        if order is not None:
            return self.db.orders.insert(order.get_as_json())
        else:
            raise Exception("Nothing to save, because order parameter is None")

    def read(self, order_id=None):
        if order_id is None:
            return self.db.orders.find({})
        else:
            return self.db.orders.find_one({"_id": ObjectId(order_id)})

    def update(self, order):
        """
         Saves order if id exists, otherwise it creates a new entry
         """
        if order is not None:
            test = self.db.orders.save(order.get_as_json())
            return test
        else:
            raise Exception("Nothing to update, because order parameter is None")
