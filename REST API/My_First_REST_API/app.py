from flask import Flask, request

app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items" : [
            {
                "name": "chair",
                "price" : 280.00
            }
        ]
    },
]

# this is our first end point
@app.get("/store") # http:127.0.0.1:5000/store
def get_store():
    return {
        "stores" : stores
    }

#default status code for any of the view function 200 i.e. everything went well
# this endpoint for creating the store
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name" : request_data['name'],
        "items" : []
    }

    stores.append(new_store)
# 201 means  accepted the data and create the store
    return new_store, 201 #status code 

# This endpoint for creating the items in specific store based pon url
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name" : request_data['name'],
                "price": request_data['price']
            }
            store['items'].append(new_item)
            return new_item, 201
    return {
        "message": "Store not found"
    }, 404 # error not found


# this is for get the data of specific store
@app.get("/store/<string:name>")
def get_store_data(name):
    for store in stores:
        if store['name'] == name:
            return store, 200
    return {
        "message" : "Store Not Found"
    }, 404


# this is for the getting the items ib the specific store
@app.get("/store/<string:name>/item")
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            store_items = store['items']
            return {"items":store_items}
    return {
        "message" : "Store Not Found"
    }, 404

    

