from db import db

class StoreModel(db.Model):
    __tablename__ = "Stores"
    id= db.Column(db.Integer , primary_key = True)
    name = db.column(db.String , Uniq = True , nullable = False)
    items = db.relationship("ItemModel" , back_populates = "store" , lazy = "dynamic")
