from django.shortcuts import render

from rest_framework.decorators import api_view

from django.http import JsonResponse
from api.models import MiniEgg, FinishedEgg

from random import randrange

# Create your views here.
@api_view(['POST'])
def create_miniegg(request):
    print(request.data)
    if "title" in request.data:
        MiniEgg.objects.create(title=request.data["title"])
        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)

@api_view(['POST'])
def pick_miniegg(request):
    print(request.data)
    if "title" in request.data:
        MiniEgg.objects.filter(title=request.data["title"])[0].delete()
        FinishedEgg.objects.create(title=request.data["title"])
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
    return JsonResponse({"title": title}, status=200)

@api_view(['GET'])
def count_minieggs(request):
    return JsonResponse({"jar": len(MiniEgg.objects.all()), "finished": len(FinishedEgg.objects.all())}, status=200)

@api_view(['GET'])
def view_minieggs(request):
    return JsonResponse({"minieggs": [x.title for x in MiniEgg.objects.all()], "finished": [x.title for x in FinishedEgg.objects.all()]}, status=200)
