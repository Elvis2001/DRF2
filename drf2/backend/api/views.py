from django.http import JsonResponse
import json
from products.models import Products


def api_home(requests, *args, **kwargs):
    model_product = Products.objects.all().order_by("?").first()

    data = {}

    if model_product:
        data['title'] = requests.title 

    return JsonResponse(data)