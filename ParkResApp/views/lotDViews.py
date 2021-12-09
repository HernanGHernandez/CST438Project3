from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view
from ParkResApp.models import User, Messages, LotA, LotB, LotC, LotD
from ParkResApp.serializers import UserSerializer, MessagesSerializer, LotASerializer, LotBSerializer, LotCSerializer, LotDSerializer
# from .filters import lotFilter


@api_view(['POST'])
def createLotD(request):
    # post methond create parking
    park_data = JSONParser().parse(request)
    parking_serializer = LotDSerializer(data=park_data)
    if parking_serializer.is_valid():
        parking_serializer.save()
        return Response("Added parking successfully")
    return Response(parking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# works


@api_view(['GET'])
def getLotD(request):
    # Get method to get parking records
    parking = LotD.objects.all()
    parking_serializer = LotDSerializer(parking, many=True)
    return Response(parking_serializer.data)

# --get all parking by userID--


@api_view(['GET'])
def userGetLotD(request, pk1):
    # Get method to get parking records by userId
    user = User.objects.filter(userId=pk1)
    parking = LotD.objects.all()
    parking_serializer = LotDSerializer(parking, many=True)
    return Response(parking_serializer.data)


@api_view(['PUT'])
def updateParkingLotD(request, pk):
    # Put method to update parking only
    parking_data = JSONParser().parse(request)
    parking = LotD.objects.get(pk=pk)
    parking_serializer = LotDSerializer(parking, data=parking_data)
    if parking_serializer.is_valid():
        parking_serializer.save()
        return Response("Updated parking Succesfully")
    return Response("Failed to update parking")


# --update parking by by userID--
@api_view(['PUT'])
def userUpdateParkingLotD(request, pk1, pk2):
    # Put method to update parking
    parking_data = JSONParser().parse(request)
    user = User.objects.filter(userId=pk1)
    parking = LotD.objects.get(LotDId=pk2)
    parking_serializer = LotDSerializer(parking, data=parking_data)
    if parking_serializer.is_valid():
        parking_serializer.save()
        return Response("Updated parking Succesfully")
    return Response("Failed to update parking")
