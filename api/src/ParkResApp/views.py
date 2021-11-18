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
from ParkResApp.models import User, Parking, Messages
from ParkResApp.serializers import UserSerializer, ParkingSerializer, MessagesSerializer
from .filters import lotFilter
# Create your views here.

#  test the app for debug mode off

# all API Views


@api_view(['GET'])
def home(request):
    api_urls = {
        'user': 'user/<str:pk>',
        'add User': 'createUser/',
        'Delete User': 'deleteUser/<str:pk>',
        'Update user': 'updateUser/<str:pk>',
        'add parking': 'createParking/',
        'parking': 'getParking/<str:pk>',
        'update Parking': 'updateParking/<str:pk>',
        'add message': 'createMessage/',
        'message': 'getMessage/<str:pk>',
        'update message': 'updateMessage/<str:pk>',
        'Get all Parking by User': 'user/userId/getParking/',
        'Update parking by User': 'user/userId/updateParking/parkingId/'
    }
    return Response(api_urls)

# -----------------User API's-------------------------


@api_view(['GET'])
def getUser(request, pk):
    # Get method to get records
    user = User.objects.filter(pk=pk)
    user_serializer = UserSerializer(user, many=True)
    return Response(user_serializer.data)


@api_view(['POST'])
def createUser(request):
    # post method to add User
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    # if data valid save into db
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("Added user successfully")
    return Response("Failed to add user")


@api_view(['PUT'])
def updateUser(request, pk):
    # Put method to update User
    user_data = JSONParser().parse(request)
    user = User.objects.get(pk=pk)
    user_serializer = UserSerializer(user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("Update user succesfully")
    return Response("Failed to update user")


@api_view(['DELETE'])
def deleteUser(request, pk):
    # Delete method
    user = User.objects.get(pk=pk)
    user.delete()
    return Response("User deleted")

# -----------------Parking API----------------------------


# error failed to add admin should create 4
@api_view(['POST'])
def createParking(request):
    # post methond create parking
    park_data = JSONParser().parse(request)
    parking_serializer = ParkingSerializer(data=park_data)
    if parking_serializer.is_valid():
        parking_serializer.save()
        return Response("Added parking successfully")
    return Response(parking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# works


@api_view(['GET'])
def getParking(request, pk):
    # Get method to get parking records
    parking = Parking.objects.filter(pk=pk)
    parking_serializer = ParkingSerializer(parking, many=True)
    return Response(parking_serializer.data)

# --get all parking by userID--


@api_view(['GET'])
def userGetParking(request, pk1):
    # Get method to get parking records by userId
    user = User.objects.filter(userId=pk1)
    parking = Parking.objects.all()
    parking_serializer = ParkingSerializer(parking, many=True)
    return Response(parking_serializer.data)


@api_view(['PUT'])
def updateParking(request, pk):
    # Put method to update parking only
    parking_data = JSONParser().parse(request)
    parking = Parking.objects.get(pk=pk)
    parking_serializer = ParkingSerializer(parking, data=parking_data)
    if parking_serializer.is_valid():
        parking_serializer.save()
        return Response("Updated parking Succesfully")
    return Response("Failed to update parking")


# --update parking by by userID--
@api_view(['PUT'])
def userUpdateParking(request, pk1, pk2):
    # Put method to update parking
    parking_data = JSONParser().parse(request)
    user = User.objects.filter(userId=pk1)
    parking = Parking.objects.get(parkingId=pk2)
    parking_serializer = ParkingSerializer(parking, data=parking_data)
    if parking_serializer.is_valid():
        parking_serializer.save()
        return Response("Updated parking Succesfully")
    return Response("Failed to update parking")

# --Get all parking by specific lot in progress--


@api_view(['GET'])
def getLot(request, pk):
    parking_serializer = ParkingSerializer

    class lotViewset(viewsets.ModelViewSet):
        parking_serializer = ParkingSerializer

        def get_queryset(self):
            parkingLot = Parking.objects.all()
            return parkingLot

        def retrieve(self, request, *args, **kwargs):
            params = kwargs

    # filterset = lotFilter(request.GET,  lot=pk)
            parkingLot = Parking.objects.filer(lot=params['pk'])
    # parking_serializer = ParkingSerializer(data=parkingLot, many=True)
            parking_serializer = ParkingSerializer(parkingLot, many=True)
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('lot', 'parkSwitch')
            return Response(parking_serializer.data)
    return Response(parking_serializer.data)


# ----------------Messages API NOT TESTED----------------------------


@api_view(['POST'])
def createMessage(request):
    # post methond create message
    message_data = JSONParser().parse(request)
    message_serializer = MessagesSerializer(data=message_data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response("Added message successfully")
    return Response("Failed to add message")


@api_view(['GET'])
def getMessage(request, pk):
    # Get method to get message records
    message = Messages.objects.filter(pk=pk)
    message_serializer = MessagesSerializer(message, many=True)
    return Response(message_serializer.data)


@api_view(['PUT'])
def updateMessage(request, pk):
    # Put method to update parking
    message_data = JSONParser().parse(request)
    message = Parking.objects.get(pk=pk)
    message_serializer = MessagesSerializer(message, data=message_data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response("Updated message Succesfully")
    return Response("Failed to update message")
