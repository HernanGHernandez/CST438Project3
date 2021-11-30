# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework import generics
# from rest_framework import viewsets

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from ParkResApp.models import User, Messages, LotA, LotB, LotC, LotD
# from ParkResApp.serializers import UserSerializer, MessagesSerializer, LotASerializer, LotBSerializer, LotCSerializer, LotDSerializer
# # from .filters import lotFilter


# @api_view(['POST'])
# def createParking(request):
#     # post methond create parking
#     park_data = JSONParser().parse(request)
#     parking_serializer = ParkingSerializer(data=park_data)
#     if parking_serializer.is_valid():
#         parking_serializer.save()
#         return Response("Added parking successfully")
#     return Response(parking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # works


# @api_view(['GET'])
# def getParking(request, pk):
#     # Get method to get parking records
#     parking = Parking.objects.filter(pk=pk)
#     parking_serializer = ParkingSerializer(parking, many=True)
#     return Response(parking_serializer.data)

# # --get all parking by userID--


# @api_view(['GET'])
# def userGetParking(request, pk1):
#     # Get method to get parking records by userId
#     user = User.objects.filter(userId=pk1)
#     parking = Parking.objects.all()
#     parking_serializer = ParkingSerializer(parking, many=True)
#     return Response(parking_serializer.data)


# @api_view(['PUT'])
# def updateParking(request, pk):
#     # Put method to update parking only
#     parking_data = JSONParser().parse(request)
#     parking = Parking.objects.get(pk=pk)
#     parking_serializer = ParkingSerializer(parking, data=parking_data)
#     if parking_serializer.is_valid():
#         parking_serializer.save()
#         return Response("Updated parking Succesfully")
#     return Response("Failed to update parking")


# # --update parking by by userID--
# @api_view(['PUT'])
# def userUpdateParking(request, pk1, pk2):
#     # Put method to update parking
#     parking_data = JSONParser().parse(request)
#     user = User.objects.filter(userId=pk1)
#     parking = Parking.objects.get(parkingId=pk2)
#     parking_serializer = ParkingSerializer(parking, data=parking_data)
#     if parking_serializer.is_valid():
#         parking_serializer.save()
#         return Response("Updated parking Succesfully")
#     return Response("Failed to update parking")

# # --Get all parking by specific lot in progress--


# @api_view(['GET'])
# def getLot(request, pk):
#     parking_serializer = ParkingSerializer

#     class lotViewset(viewsets.ModelViewSet):
#         parking_serializer = ParkingSerializer

#         def get_queryset(self):
#             parkingLot = Parking.objects.all()
#             return parkingLot

#         def retrieve(self, request, *args, **kwargs):
#             params = kwargs

#     # filterset = lotFilter(request.GET,  lot=pk)
#             parkingLot = Parking.objects.filer(lot=params['pk'])
#     # parking_serializer = ParkingSerializer(data=parkingLot, many=True)
#             parking_serializer = ParkingSerializer(parkingLot, many=True)
#     # filter_backends = (DjangoFilterBackend, SearchFilter)
#     # filter_fields = ('lot', 'parkSwitch')
#             return Response(parking_serializer.data)
#     return Response(parking_serializer.data)
