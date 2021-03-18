from flask_restplus import fields
from app.api.restconfig import api


save_order = api.model(
    "Vehicle Order Creation",
    {
        "vehicle_manufacturer": fields.String(
            required=True, description="The Vehicle Manufacturer"
        ),
        "model": fields.String(required=True, description="The Vehicle Model"),
        "total_price": fields.Float(required=True, description="The Total Price"),
    },
)

order = api.inherit(
    "Vehicle Order",
    save_order,
    {
        "_id": fields.String(required=True, description="The Order Identifier"),
    },
)
