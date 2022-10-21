from marshmallow import Schema
from marshmallow import fields

from services.utils import get_objects


class UserSchema(Schema):
    id = fields.Method('get_new_id')
    rol = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    type = fields.Str(dump_default='User')

    def get_new_id(self, obj):
        return get_objects('User')[-1]['id'] + 1
