import requests

# endpoint = 'https://httpbin.org/status/200'
endpoint = 'http://localhost:8000/api/'  # http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={'title': 'Hi!', 'price': 123, 'content': 'Hello world!'})  # HTTP response
# print(get_response.headers)
# print(get_response.text)  # print raw text response
# print(get_response.status_code)
print(get_response.json())
