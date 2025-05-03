from flask import Flask, request

app = Flask(__name__)

stores = [
    {"name" : "My Store",
    "address" : "Burnaby",
     "items" : [{
         "name" : "Chair",
         "price" : 15.99
     }
     ]
}
]


@app.get('/store')
def get_stores():
    return {'stores' : stores}

@app.post('/store')
def create_store():
    new_store = {"name" : "test_1", "items" : []}
    stores.append(new_store)
    return stores, 201

@app.post('/store/<string:name>/item')
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name" : name, "price" : request_data["price"]}
            store['items'].append(new_item)
            return new_item, 201
    return {"message" : "Item not found"}, 404



if __name__ == '__main__':
    app.run()
