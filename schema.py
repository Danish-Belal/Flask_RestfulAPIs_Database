from marshmallow import Schema, fields


class PlanItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    
 
class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class ItemSchema(PlanItemSchema):
    store_id = fields.Int(required = True , load_only = True)
    store = fields.Nested(PlainStoreSchema() , dump_only= True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlanItemSchema() , dump_only = True))


