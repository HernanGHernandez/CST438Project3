from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from ParkResApp.models import User, Parking, Messages
from ParkResApp.serializers import UserSerializer, ParkingSerializer, MessagesSerializer
# Create your views here.

#  test the app for debug mode off

# all API Views


@api_view(['GET'])
def home(request):
    api_urls = {
        'user': 'user/<str:pk>',
        'addUser': 'createUser/',
        'Delete': 'deleteUser/<str:pk>',
        'Update': 'updateUser/<str:pk>'
    }
    return Response(api_urls)

# User API's


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
        return Response("Added successfully")
    return Response("Failed to add user")


@api_view(['PUT'])
def updateUser(request, pk):
    # Put method to update User
    user_data = JSONParser().parse(request)
    user = User.objects.get(pk=pk)
    user_serializer = UserSerializer(user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("Update Succesfull")
    return Response("Failed to update")


@api_view(['DELETE'])
def deleteUser(request, pk):
    # Delete method
    user = User.objects.get(pk=pk)
    user.delete()
    return Response("User deleted")
