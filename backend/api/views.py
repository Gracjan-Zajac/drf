import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> Django HttpRequest instance
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse({'message': 'Hi, this is your Django API response!'})
