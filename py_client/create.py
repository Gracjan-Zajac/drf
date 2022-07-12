import requests

headers = {'Authorization': 'Bearer aa257845257e6701ebe39414b3b7e0d75758ae44'}
endpoint = "http://localhost:8000/api/products/"

data = {"title": "New Product"}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
