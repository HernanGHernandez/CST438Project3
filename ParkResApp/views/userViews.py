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
# Create your views here.


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
