from flask import request
from flask_restful import abort
from flask_restful import Resource

from fake_db import FAKE_DB
from serializers.location import LocationSchema
from services.utils import get_objects


class ListLocations(Resource):
    def get(self):
        return get_objects('Location')


class CreateLocation(Resource):
    def post(self):
        args = request.json
        new_location = LocationSchema().dump(args)
        FAKE_DB.append(new_location)
        return new_location, 200


class Location(Resource):
    def get(self, location_id):
        for location in get_objects('Location'):
            if location['id'] == int(location_id):
                return location
        abort(404, message="Location {} doesn't exist".format(location_id))

    def delete(self, location_id):
        for location in get_objects('Location'):
            if location['id'] == int(location_id):
                location.update({
                    'delete': True
                })
                return location
        abort(404, message="Location {} doesn't exist".format(location_id))

    def put(self, location_id):
        args = request.json
        for location in get_objects('Location'):
            if location['id'] == int(location_id):
                location.update(args)
                return location
        abort(404, message="Location {} doesn't exist".format(location_id))
