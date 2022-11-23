from marshmallow import Schema
from marshmallow import fields

from services.utils import get_objects


class AssetSchema(Schema):
    id = fields.Method('get_new_id')
    code = fields.Str()
    denomination = fields.Str()
    brand = fields.Str()
    model = fields.Str()
    color = fields.Str()
    serie = fields.Str()
    e = fields.Str()
    gp = fields.Str()
    detail = fields.Str()
    dimensions = fields.Str()
    location = fields.Integer()
    inventory = fields.Integer()
    type = fields.Str(dump_default='Asset')

    def get_new_id(self, obj):
        return get_objects('Asset')[-1]['id'] + 1
