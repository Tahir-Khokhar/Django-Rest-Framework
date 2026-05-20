# from django.shortcuts import render
# from django.http import JsonResponse
# # Create your views here.

# def api_home(request, *args, **kwargs):
#     body = request.body # byte string of JSON data
#     print(body)
#     return JsonResponse({'message': 'Hi! This is your first API response'})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> dict
    except:
        pass
    print(data)
    # data['header'] = request.headers # request.META
    print(request.headers)
    data['headers']=(dict(request.headers))
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type 
    return JsonResponse({'message': 'Hi! This is your first API response'})