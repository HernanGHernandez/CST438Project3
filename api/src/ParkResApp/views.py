from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

#  test the app for debug mode off
# test for heruko deployment


def ping(request):
    data = {'ping': 'pong!'}
    return JsonResponse(data)
