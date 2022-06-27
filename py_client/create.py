import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "This one is done", "content": "Let's see..."}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
