from bson.objectid import ObjectId


class Order(object):
    def __init__(
            self, order_id=None, vehicle_manufacturer=None, model=None, total_price=0.0
    ):
        if order_id is None:
            self._id = ObjectId()
        else:
            self._id = order_id
        self.vehicle_manufacturer = vehicle_manufacturer
        self.model = model
        self.total_price = total_price

    def get_as_json(self):
        """
        Method returns the JSON representation of the Order object
        """
        return self.__dict__

    @staticmethod
    def build_and_validate(json_data):
        if json_data is not None:
            try:
                return Order(
                    json_data.get("_id", None),
                    json_data["vehicle_manufacturer"],
                    json_data["model"],
                    json_data["total_price"],
                )

            except KeyError as e:
                raise Exception(f"Key not found in json_data: {e}")
        else:
            raise Exception("No data to create Project from!")
