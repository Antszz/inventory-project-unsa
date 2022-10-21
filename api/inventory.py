from flask import request
from flask_restful import Resource

from fake_db import FAKE_DB
from serializers.inventory import InventorySchema
from services.utils import get_objects


class Inventories(Resource):
    def get(self):
        return get_objects('Inventory')

    def post(self):
        args = request.json
        new_inventory = InventorySchema().dump(args)
        FAKE_DB.append(new_inventory)
        return new_inventory, 200
