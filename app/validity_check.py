from datetime import datetime, timedelta

import requests

from sending_mail import send_mail

BASE_URL = 'http://127.0.0.1:5000/admin/v1/'
API_APIKEYS = 'ApiKeys'
API_LIST_USERS = 'list_users'


def is_key_expired(user_id, user_mail):
    threshold_date = datetime.utcnow() - timedelta(days=90)

    url = BASE_URL + API_APIKEYS + '/' + user_id

    response = requests.get(url)

    api_key_data = response.json()

    created_date = datetime.strptime(api_key_data["meta"]["created"], "%Y-%m-%dT%H:%M:%SZ")

    if created_date < threshold_date:
        send_mail(api_key_data['id'], api_key_data['user']['name'], user_mail)
        return True
    return False


def check_users_keys():
    checked_keys = {}

    url = BASE_URL + API_LIST_USERS
    response = requests.get(url)
    list_of_users = response.json()

    for user in list_of_users['list_users']:
        user_identifier = user['id'].split('.')[-1]
        is_expired = is_key_expired(user_identifier, user['email'])

        if is_expired:
            checked_keys[user_identifier] = (user['email'], "Expired")
        else:
            checked_keys[user_identifier] = (user['email'], "Valid")
    return checked_keys
