from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from api.asset import Asset
from api.asset import CreateAsset
from api.asset import ListAssets
from api.inventory import Inventory
from api.inventory import CreateInventory
from api.inventory import ListInventories
from api.location import Location
from api.location import CreateLocation
from api.location import ListLocations
from api.user import ListUsers
from api.user import User
from api.user import CreateUser
# from flask_mongoengine import MongoEngine

app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#         "db": "inventory-unsa",
#     }
# db = MongoEngine(app)
CORS(app)
api = Api(app)

api.add_resource(Inventory, '/inventory/<inventory_id>')
api.add_resource(CreateInventory, '/inventory')
api.add_resource(ListInventories, '/inventories')

api.add_resource(Asset, '/asset/<asset_id>')
api.add_resource(CreateAsset, '/asset')
api.add_resource(ListAssets, '/assets')

api.add_resource(User, '/user/<user_id>')
api.add_resource(CreateUser, '/user')
api.add_resource(ListUsers, '/users')

api.add_resource(Location, '/location/<location_id>')
api.add_resource(CreateLocation, '/location')
api.add_resource(ListLocations, '/locations')

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(debug=True)
