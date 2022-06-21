import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> Django HttpRequest instance
    print(request.GET)  # URL query params
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
