import json
import os

from flask import Flask, render_template, jsonify, request

from validity_check import check_users_keys

app = Flask(__name__)


@app.route('/admin/v1/ApiKeys/<api_key_id>', methods=['GET'])
def get_api_key(api_key_id):
    file_path = os.path.join(f"mock_responses/{api_key_id}.json")

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            api_key_data = json.load(file)
            return jsonify(api_key_data), 200
    else:
        return jsonify({"error": "API key not found"}), 404


@app.route('/admin/v1/list_users', methods=['GET'])
def mock_list_users():
    file_path = os.path.join(f"mock_responses/list_users.json")

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            list_of_users = json.load(file)
            return jsonify(list_of_users), 200
    else:
        return jsonify({"error": "API key not found"}), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    checked_keys = {}
    if request.method == 'POST':
        checked_keys.update(check_users_keys())

    return render_template('index.html', checked_keys=checked_keys)


if __name__ == '__main__':
    app.run(debug=True)
