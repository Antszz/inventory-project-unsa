from flask import request
from flask_restful import abort
from flask_restful import Resource

from fake_db import FAKE_DB
from serializers.inventory import InventorySchema
from services.utils import get_objects


class ListInventories(Resource):
    def get(self):
        return get_objects('Inventory')


class CreateInventory(Resource):
    def post(self):
        args = request.json
        new_inventory = InventorySchema().dump(args)
        FAKE_DB.append(new_inventory)
        return new_inventory, 200


class Inventory(Resource):
    def get(self, inventory_id):
        for inventory in get_objects('Inventory'):
            if inventory['id'] == int(inventory_id):
                return inventory
        abort(404, message="inventory {} doesn't exist".format(inventory_id))

    def delete(self, inventory_id):
        for inventory in get_objects('Inventory'):
            if inventory['id'] == int(inventory_id):
                inventory.update({
                    'delete': True
                })
                return inventory
        abort(404, message="inventory {} doesn't exist".format(inventory_id))

    def put(self, inventory_id):
        args = request.json
        for inventory in get_objects('Inventory'):
            if inventory['id'] == int(inventory_id):
                inventory.update(args)
                return inventory
        abort(404, message="inventory {} doesn't exist".format(inventory_id))
