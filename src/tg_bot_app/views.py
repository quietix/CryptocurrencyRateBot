from . import request_handler
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def handle_request(request):
    if request.method == "POST":
        try:
            request_body = json.loads(request.body)
            request_handler.handle_request(request_body)
        except Exception as e:
            print(str(e))
        return HttpResponse('', status=200)
    else:
        return Http404