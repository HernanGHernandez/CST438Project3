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
# from .filters import lotFilter


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


@csrf_exempt
@api_view(['POST'])
def createMessage(request):
    # post methond create message
    message_data = JSONParser().parse(request)
    message_serializer = MessagesSerializer(data=message_data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response("Added message successfully")
    return Response(message_serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getMessage(request, pk):
    # Get method to get message records
    message = Messages.objects.filter(pk=pk)
    message_serializer = MessagesSerializer(message, many=True)
    return Response(message_serializer.data)


@api_view(['PUT'])
def updateMessage(request, pk):
    # Put method to update parking
    try:
        message = Messages.objects.get(pk=pk)
    except Messages.DoesNotExist:
        return JsonResponse('does not exist', status=status.HTTP_404_NOT_FOUND)

    message_data = JSONParser().parse(request)
    message_serializer = MessagesSerializer(message, data=message_data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response("Updated message Succesfully")
    return Response(message_serializer.errors, status=status.HTTP_404_NOT_FOUND)
