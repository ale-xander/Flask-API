from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'alex'

#create /auth endpoint which returns a JWT token. can send to next request we send
jwt = JWT(app, authenticate, identity) #use jwt in app and authenticate/identity from security.py

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        #first item found by filter function. None is in case it didn't find anything
        item = next(filter(lambda x: x['name'] == name, items), None) 
        #now return item or None
        return {'item': item}, 200 if item else 404
    
    def post(self, name):
        #if item found and it is not None
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'this item already exists'}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)