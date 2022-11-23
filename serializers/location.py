from marshmallow import Schema
from marshmallow import fields

from services.utils import get_objects


class LocationSchema(Schema):
    id = fields.Method('get_new_id')
    code = fields.Str()
    location_type = fields.Str()
    type = fields.Str(dump_default='Location')

    def get_new_id(self, obj):
        return get_objects('Location')[-1]['id'] + 1
