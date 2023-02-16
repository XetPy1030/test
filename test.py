import requests
import json


# base_url = 'http://127.0.0.1:8000/api/v1/'
base_url = 'http://dellavrite.ru/api/v1/'

def post():
    with open("./src/apps/hr_department/tests/data.json", encoding="utf-8") as f:
        data = json.load(f)

    data.update({
        'full_name': 'Yyyy',
        'is_editable': 'false',
        'user_id': "test",
        'owner_id': "test",
    })

    print(data)

    requests.post(
        base_url + 'admin/save/',
        json=data
    )


def get():
    response = requests.get(
        base_url + f'user/save/?user_id=test',
    )
    print(response.json(), response.status_code)

post()
get()