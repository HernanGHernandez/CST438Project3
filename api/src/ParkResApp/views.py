from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ParkResApp.models import User, Parking, Messages
from ParkResApp.serializers import UserSerializer, ParkingSerializer, MessagesSerializer
# Create your views here.

#  test the app for debug mode off
# test for heruko deployment


def home(request):
    data = {'test': 'json!'}
    return JsonResponse(data)


@csrf_exempt
def userApi(request, id=100):
    # Get method to get records
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    # post method to add User
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        # if data valid save into db
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add user", safe=False)
    # Put method to update User
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data['userId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update Succesfull", safe=False)
        return JsonResponse("Failed to update")
    # Delete method
    elif request.method == 'DELETE':
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse("User deleted", safe=False)
