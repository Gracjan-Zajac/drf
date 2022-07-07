import requests

endpoint = "http://localhost:8000/api/products/2/update/"

data = {
    'title': 'new title',
    'content': '',
    'price': 60
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
