from marshmallow import Schema
from marshmallow import fields

from services.utils import get_objects


class InventorySchema(Schema):
    id = fields.Method('get_new_id')
    recorder = fields.Integer()
    receiver = fields.Integer()
    location = fields.Integer()
    assets = fields.List(fields.Integer(), dump_default=list)
    type = fields.Str(dump_default='Inventory')

    def get_new_id(self, obj):
        return get_objects('Inventory')[-1]['id'] + 1


class ListInventorySchema(Schema):
    id = fields.Integer()
    recorder = fields.Method('get_recorder')
    receiver = fields.Method('get_receiver')
    location = fields.Method('get_location')
    assets = fields.Method('get_assets')
    type = fields.Str(dump_default='Inventory')

    def get_assets(self, obj):
        assets = []
        for asset in get_objects('Asset'):
            if asset['id'] in obj['assets']:
                assets.append(asset)
        return assets

    def get_location(self, obj):
        for location in get_objects('Location'):
            if location['id'] == obj['location']:
                return location

    def get_recorder(self, obj):
        for recorder in get_objects('User'):
            if recorder['id'] == obj['recorder']:
                return recorder

    def get_receiver(self, obj):
        for receiver in get_objects('User'):
            if receiver['id'] == obj['receiver']:
                return receiver
