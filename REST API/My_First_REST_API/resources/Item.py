import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort # type: ignore
from db import items, stores

# This is file is the same as the store.py But 
# In this file their is just operations on the Items in the store

blp = Blueprint("Items", __name__, description="Operations on item")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
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

    def put(self, item_id):
        new_item_data = request.get_json()
    
        if 'item_price' not in new_item_data or 'item_name' not in new_item_data:
            abort(400, message="Bad request, Ensure that 'item_price' and 'item_name' is present in JSON payload")

        try:
            item = items[item_id]
            item |= new_item_data

            return item
        except KeyError:
            abort(404, "Item not found.")



@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items" : list(items.values())}

    def post(self):
        item_data = request.get_json()
        # this for checking the JSON payload is correct or not
        if(
            "item_name" not in item_data
            or "item_price" not in item_data
            or "store_id" not in item_data
        ):
            abort(400, message="Bad request, make sure 'item_name', 'item_price' and 'store_id' are included in the JSON payload")
        
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