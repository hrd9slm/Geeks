from flask import Flask, request, jsonify
from flask_cors import CORS
from menu_item import MenuItem
from menu_manager import MenuManager

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "API is running"}), 200


@app.route("/menu", methods=["POST"])
def create_item():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    
    if not name or price is None:
        return jsonify({"error": "Missing name or price"}), 400

    item = MenuItem(name, price)
    item.save()
    return jsonify({"message": f"Item '{name}' created"}), 201


@app.route("/menu", methods=["GET"])
def get_all_items():
    items = MenuManager.all()
    return jsonify(items), 200


@app.route("/menu/<string:name>", methods=["GET"])
def get_item(name):
    item = MenuManager.get_by_name(name)
    if item:
        return jsonify(item), 200
    return jsonify({"error": f"Item '{name}' not found"}), 404


@app.route("/menu/<string:name>", methods=["PUT"])
def update_item(name):
    data = request.get_json()
    new_name = data.get("name")
    new_price = data.get("price")

    if new_name is None or new_price is None:
        return jsonify({"error": "Missing new name or new price"}), 400

    item_data = MenuManager.get_by_name(name)
    if not item_data:
        return jsonify({"error": f"Item '{name}' not found"}), 404

    item = MenuItem(item_data["item_name"], item_data["item_price"])
    item.update(new_name, new_price)
    return jsonify({"message": f"Item '{name}' updated to '{new_name}' with price {new_price}"}), 200


@app.route("/menu/<string:name>", methods=["DELETE"])
def delete_item(name):
    item_data = MenuManager.get_by_name(name)
    if not item_data:
        return jsonify({"error": f"Item '{name}' not found"}), 404

    item = MenuItem(item_data["item_name"], item_data["item_price"])
    item.delete()
    return jsonify({"message": f"Item '{name}' deleted"}), 200

if __name__ == "__main__":
    app.run(port=8000, debug=True)
   