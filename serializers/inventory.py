from marshmallow import Schema
from marshmallow import fields

from services.utils import get_objects


class InventorySchema(Schema):
    id = fields.Method('get_new_id')
    recorder = fields.Integer()
    receiver = fields.Integer()
    location = fields.Str()
    assets = fields.List(fields.Integer(), dump_default=list)
    type = fields.Str(dump_default='Inventory')

    def get_new_id(self, obj):
        return get_objects('Inventory')[-1]['id'] + 1
