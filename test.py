import requests
import json

with open("./src/apps/hr_department/tests/data.json", encoding="utf-8") as f:
    data = json.load(f)

data.update({
    'is_editable': 'true',
    'user_id': "test",
    'owner_id': "test",
})

print(data)

requests.post(
    'http://127.0.0.1:8000/api/v1/admin/save/',
    json=data
)