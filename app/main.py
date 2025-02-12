import json
import os

from flask import Flask, render_template, jsonify, request

from mock_responses.list_users_response import list_users
from validity_check import is_key_expired


app = Flask(__name__)


@app.route('/admin/v1/ApiKeys/<api_key_id>', methods=['GET'])
def get_api_key(api_key_id):
    file_path = os.path.join(f"mock_responses/{api_key_id}.json")

    # Check if the file exists
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            # Read the JSON content from the file
            api_key_data = json.load(file)
            return jsonify(api_key_data), 200
    else:
        return jsonify({"error": "API key not found"}), 404


# TODO: finish list_users mock
def mock_list_users():
    return list_users


@app.route('/', methods=['GET', 'POST'])
def index():

    checked_keys = {}
    if request.method == 'POST':
        list_of_users = mock_list_users()
        for user in list_of_users:
            user_identifier = user.id.split('.')[-1]
            is_expired = is_key_expired(user_identifier, user.email)

            if is_expired:
                checked_keys[user_identifier] = (user.email, "Expired")
            else:
                checked_keys[user_identifier] = (user.email, "Valid")

    return render_template('index.html', checked_keys=checked_keys)


if __name__ == '__main__':
    app.run(debug=True)
    # app.py.run()
