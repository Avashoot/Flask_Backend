import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort # type: ignore
from db import stores
from schemas import StoreSchema

# The Blueprint in flask_smorest used to divide API into multiple segments
# Here instance of Blueprint class thats  come with the 3 attributes
# .............<name_tag>, gating_name, desc of the instance
blp = Blueprint("stores", __name__, description="Operations on store")

# blp.route used for the routing with the different API's just like the 
# app.get(), .post(), .put(), .delete()
# instead of using same routing again and again we create teh class of the same 
#  routing  methods, here comes the use of BluePrint flask smorest
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # The above MethodView is a class its get Inherited By the classes  for creating
    # the classes and their routing or REST methods in flask
    # the below get() method act as app.get("url/<id>")
    # this get() method is for the information about that store
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    #  this delete() delete the store data
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message":"Store deleted"}
        except KeyError:
            abort(404, message="Store not found")


@blp.route("/store")
class StoreList(MethodView):
    # this is for the get the data of the all the stores
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values() # return list because StoreSchema(many=True)

    # this is for the add the new store in the database
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
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
