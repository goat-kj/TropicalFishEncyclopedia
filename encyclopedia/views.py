from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fish, Region
from .serializers import FishSerializer, RegionSerializer

@api_view(['GET'])
def getRegionInfo(request):
    region = Region.objects.all()
    serializer = RegionSerializer(region, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllFish(request):
    fish = Fish.objects.all()
    serializer = FishSerializer(fish, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFishInfo(request, pk):
    fish = Fish.objects.get(id=pk)
    serializer = FishSerializer(fish, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addFishInfo(request):
    serializer = FishSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def updateFishInfo(request, pk):
    fish = Fish.objects.get(id=pk)
    serializer = FishSerializer(instance=fish, data=request.data)
    if serializer.is_valid():
        serializer.save()    
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteFishInfo(request, pk):
    fish = Fish.objects.get(id=pk)
    fish.delete()
    return Response("Fish Info Deleted.")