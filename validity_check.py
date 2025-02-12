from datetime import datetime, timedelta

import requests

from sending_mail import send_mail

# TODO: updates api address to oracle
BASE_URL = 'http://127.0.0.1:5000/admin/v1/ApiKeys/'


def is_key_expired(user_id, user_mail):
    threshold_date = datetime.utcnow() - timedelta(days=90)

    diec = BASE_URL + user_id

    response = requests.get(diec)

    api_key_data = response.json()

    created_date = datetime.strptime(api_key_data["meta"]["created"], "%Y-%m-%dT%H:%M:%SZ")

    if created_date < threshold_date:
        send_mail(api_key_data['id'], api_key_data['user']['name'], user_mail)
        return True
    return False
