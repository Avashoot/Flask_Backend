from flask import Flask, request
from db import items, stores
from flask_smorest import abort # type: ignore
import uuid

app = Flask(__name__)




# this is our first end point
@app.get("/store") # http:127.0.0.1:5000/store
def get_store():
    return {
        "stores" : list(stores.values())
    }

#default status code for any of the view function 200 i.e. everything went well
# this endpoint for creating the store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "store_name" not in store_data:
        abort(400, "Bad request, ensure 'store_name' is included in JSON payload")
    
    for store in stores.values():
        if store["store_name"] == store_data["store_name"]:
            abort(400, message="Store already exists.")
    store_id = uuid.uuid4().hex #long string of numbers and letters
    new_store = {
        **store_data,
        "store_id" : store_id
    }

    stores[store_id] = new_store
# 201 means  accepted the data and create the store
    return new_store, 201 #status code 

# This endpoint for creating the items in items dictionary
@app.post("/item")
def create_item():
    
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

# get all items
@app.get("/item")
def get_all_items():
    return {"items" : list(items.values())}


# this is for get the data of specific store
@app.get("/store/<string:store_id>")
def get_store_data(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


# this is for the getting the specific item
@app.get("/item/<string:item_id>")
def get_store_items(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")

#
# delete store form the data
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message":"Item deleted"}
    except KeyError:
        abort(404, message="Item not found")

# delete store from the data
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message":"Store deleted"}
    except KeyError:
        abort(404, message="Store not found")


# update the item in the data
@app.put("/item/<string:item_id>")
def update_item(item_id):
    new_item_data = request.get_json()
    
    if 'item_price' not in new_item_data or 'item_name' not in new_item_data:
        abort(400, message="Bad request, Ensure that 'item_price' and 'item_name' is present in JSON payload")

    try:
        item = items[item_id]
        item |= new_item_data

        return item
    except KeyError:
        abort(404, "Item not found.")
    