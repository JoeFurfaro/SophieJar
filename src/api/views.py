from django.shortcuts import render

from rest_framework.decorators import api_view

from django.http import JsonResponse
from api.models import MiniEgg

from random import randrange

# Create your views here.
@api_view(['POST'])
def create_miniegg(request):
    print(request.data)
    if "title" in request.data:
        MiniEgg.objects.create(title=request.data["title"])
        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)

@api_view(['GET'])
def grab_miniegg(request):
    if len(MiniEgg.objects.all()) == 0:
        return JsonResponse({}, status=404)
    objects = MiniEgg.objects.all()
    index = randrange(0, len(objects))
    obj = objects[index]
    title = obj.title
    obj.delete()
    return JsonResponse({"title": title}, status=200)

@api_view(['GET'])
def count_minieggs(request):
    return JsonResponse({"count": len(MiniEgg.objects.all())}, status=200)

@api_view(['GET'])
def view_minieggs(request):
    return JsonResponse({"minieggs": [x.title for x in MiniEgg.objects.all()]}, status=200)
