from flask import Flask
from flask_restful import Api
from api.asset import Assets
from api.inventory import Inventories
from api.user import ListUser
from api.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(Inventories, '/inventories')
api.add_resource(Assets, '/assets/<asset_id>')
api.add_resource(User, '/user/<user_id>')
api.add_resource(ListUser, '/users')


if __name__ == '__main__':
    app.run(debug=True)
