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
