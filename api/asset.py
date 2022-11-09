from flask import request
from flask_restful import abort
from flask_restful import Resource

from fake_db import FAKE_DB
from serializers.asset import AssetSchema
from services.utils import get_objects


class ListAssets(Resource):
    def get(self):
        return get_objects('Asset')


class CreateAsset(Resource):
    def post(self):
        args = request.json
        new_asset = AssetSchema().dump(args)
        FAKE_DB.append(new_asset)
        return new_asset, 200


class Asset(Resource):
    def get(self, asset_id):
        for asset in get_objects('Asset'):
            if asset['id'] == int(asset_id):
                return asset
        abort(404, message="Asset {} doesn't exist".format(asset_id))

    def delete(self, asset_id):
        for asset in get_objects('Asset'):
            if asset['id'] == int(asset_id):
                asset.update({
                    'delete': True
                })
                return asset
        abort(404, message="Asset {} doesn't exist".format(asset_id))

    def put(self, asset_id):
        args = request.json
        for asset in get_objects('Asset'):
            if asset['id'] == int(asset_id):
                asset.update(args)
                return asset
        abort(404, message="Asset {} doesn't exist".format(asset_id))
