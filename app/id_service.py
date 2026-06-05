from flask import Flask, request, jsonify
import json
import random
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "ids.json")

# Helper: load IDS
def load_ids():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
# Helper: save IDs
def save_ids(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=2)

# Generate ID
@app.route('/generate-id', methods=['GET'])
def generate_id():
    prefix = request.args.get('prefix', 'ID')

    data = load_ids()

    # Create random Number
    random_number = random.randint(1000, 9999)
    new_id = f"{prefix}-{random_number}"

    # Ensure uniqueness
    existing_ids = [item["id"] for item in data["ids"]]
    while new_id in existing_ids:
        random_number = random.randint(1000, 9999)
        new_id = f"{prefix}-{random_number}"
    
    # Save ID
    data["ids"].append({"id": new_id})
    save_ids(data)

    return jsonify({
        "generated_id": new_id
    })


# Get all IDS
@app.route('/ids', methods=['Get'])
def get_ids():
    data = load_ids()
    return jsonify(data)

# Run server
if __name__ == '__main__':
    app.run(debug=True)