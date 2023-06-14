import uuid
from flask import Flask , request
from flask_smorest import abort
from db import stores , items


app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"Stores" : list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "Name" not in store_data:
        abort(400, 
              massage = "Name is not Present")
    store_id = uuid.uuid4().hex
    store = {**store_data , "id" : store_id}
    stores[store_id] = store
    return store, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, massage = "Store not found")

@app.delete("/store/<string:store_id>")
def deleteStore(store_id):
    try:
        del stores[store_id]
        return {"massage" : "Store Deleted"}
    except KeyError:
        return{"massage" : "Store Not Found"}


            # <-----------------Items ------------------------>

@app.get("/item")
def get_all_items():
    return {"items" : list(items.values())}


@app.post("/item")
def create_item():
    item_data = request.get_json()
    if(
        "Price" not in item_data
        or "Name" not in item_data
        or "store_id" not in item_data

    ):
        abort(400 ,
            massage  = "Bad request. Ensure 'Price', 'Name' , 'store-Id' ")
    
    item_id = uuid.uuid4().hex
    item = {**item_data , "id": item_id} 
    items[item_id] = item
    return item, 201


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404 , massage = "Item not found")


@app.put("/item/<string:item_id>")
def updateItem(item_id):
    new_item = request.get_json()
    if "Name" and "Price" not in new_item:
        abort(404 , massage = "Ensure to provide Name and Price")
    try:
        item = items[item_id]
        item |= new_item
        return item
    except KeyError:
        abort(404, massage = "Item Not Found")


@app.delete("/item/<string:item_id>")
def deleteItem(item_id):
    try:
        del items[item_id]
        return {"massage" : "Item deleted."}
    except KeyError:
        abort(404, massage = "Item Not Found")



