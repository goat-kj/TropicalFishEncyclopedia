from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from .models import Fish, Region, Staff, Message
from .serializers import FishSerializer, RegionSerializer, StaffSerializer, MessageSerializer


#Regions
@api_view(['GET'])
def getRegionInfo(request):
    region = Region.objects.all()
    serializer = RegionSerializer(region, many=True)
    return Response(serializer.data)

#Staffs
@api_view(['GET'])
def getStaff(request, pk):
    staff = Staff.objects.get(id=pk)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)

#Fish
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
    print(request.data['data'])
    serializer = FishSerializer(data=request.data['data'])
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

#Messages
@api_view(['GET'])
def getAllMessages(request):
    message = Message.objects.all()
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewMessage(request, pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createMessage(request):
    print(request.data['data'])
    serializer = MessageSerializer(data=request.data['data'])
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()
    return Response("Message Deleted.")