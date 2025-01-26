import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort # type: ignore
from db import items, stores
from schemas import ItemSchema, UpdateItemSchema

# This is file is the same as the store.py But 
# In this file their is just operations on the Items in the store

blp = Blueprint("Items", __name__, description="Operations on item")

@blp.route("/item/<string:item_id>")
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message":"Item deleted"}
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(UpdateItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, new_item_data, item_id):
        # we need to put new_item_data just after the self
        try:
            item = items[item_id]
            item |= new_item_data

            return item
        except KeyError:
            abort(404, "Item not found.")



@blp.route("/item")
class ItemList(MethodView):
    #here we are using marshmallow for validation and response
    # so while returning before we are using {"items" : list(items.values())}
    # But now ItemSchema(many=True) at the beginning 
    # while returning already it convert it into lis so, just return 
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return items.values() #this will now return a list of items not a object with list of items

    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        # we are now using the marshmallow schemas for validation purposes
        # so, we don't need tp use request.get_json() shown below
        # item_data = request.get_json()
        # this for checking the JSON payload is correct or not
        # check teat the same item is not added twice
        for item in items.values():
            if (
                item_data["item_name"] == item["item_name"]
                and item_data["store_id"] == item["store_id"]
                ):
                abort(400, message="Item already exists")

        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
        
        item_id = uuid.uuid4().hex
        item = {
            **item_data,
            "item_id": item_id
        }

        items[item_id] = item
        return item, 201