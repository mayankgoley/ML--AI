### Put and Delete - HTTP verbs
### Working with API's - Json

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in our to-do list
items = [
    {"id": 1, "name": "Item 1" , "Description": "This is item 1"},
    {"id": 2, "name": "Item 1" , "Description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample to-do list."

## GET - Retrieve all the items

@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

## Retrieve specific item by id

@app.route('/items/<int: item_id>', methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify("error: item not found")
    return item



if __name__ =='__main__':
    app.run(debug=True)


