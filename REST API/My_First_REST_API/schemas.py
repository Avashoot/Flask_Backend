from marshmallow import Schema, fields

class PlaneItemSchema(Schema):
    item_id = fields.Str(dump_only= True)
    item_name = fields.Str(required=True)
    item_price = fields.Float(required= True)


class PlaneStoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    store_name = fields.Str(required=True)

class UpdateItemSchema(Schema):
    item_name = fields.Str()
    item_price = fields.Float()
    store_id = fields.Int()



'''
because in python we cannot use the function or class before it get declare 
so that, if we write a following two class without using PlaneItemSchema and
PlaneStoreSchema the code goes into infinite looping as shown below

because StoreSchema is not declare yet so we need to use lambda function
class ItemSchema(Schema):
    store_id= fields.Str(required=True)
    store = fields.Nested(lambda : StoreSchema(), dump_only= True)


class StoreSchema(Schema):
    items = fields.List(fields.Nested(lambda : ItemSchema(), dump_only = True))

above two schema uo se that flows goes to ItemSchema-> StoreSchema-> ItemSchema-> StoreSchema-> ItemSchema-> StoreSchema-> ItemSchema-> StoreSchema-> .....

so that we need to use PlaneStoreSchema, PlaneItemSchema

'''

class ItemSchema(PlaneItemSchema):
    store_id= fields.Int(required=True)
    store = fields.Nested(PlaneStoreSchema, dump_only= True)


class StoreSchema(PlaneStoreSchema):
    items = fields.List(fields.Nested(PlaneItemSchema, dump_only = True))


