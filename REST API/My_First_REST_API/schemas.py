from marshmallow import Schema, fields

class ItemSchema(Schema):
    item_id = fields.Str(dump_only= True)
    item_name = fields.Str(required=True)
    item_price = fields.Float(required= True)
    store_id = fields.Str(required= True)


class UpdateItemSchema(Schema):
    item_name = fields.Str()
    item_price = fields.Float()


class StoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    store_name = fields.Str(required=True)

