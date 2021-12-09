from django.conf.urls import url
from ParkResApp import views
from django.urls import path
from ParkResApp.views import messageViews, userViews, lotAViews, lotBViews, lotCViews, lotDViews


urlpatterns = [
    path('', messageViews.home, name='home'),
    path('user/<int:pk>', userViews.getUser, name='getUser'),
    path('updateUser/<int:pk>', userViews.updateUser, name='updateUser'),
    path('deleteUser/<int:pk>', userViews.deleteUser, name='deleteUser'),
    path('createUser/', userViews.createUser, name='createUser'),

    #     # ---parking-urls---
    #     path('createParking/', parkingViews.createParking, name='createParking'),
    #     path('getParking/<int:pk>', parkingViews.getParking, name='getParking'),
    #     path('updateParking/<str:pk>',
    #          parkingViews.updateParking, name='updateParking'),
    #     path('user/<str:pk1>/getParking/',
    #          parkingViews.userGetParking, name='userGetParking'),
    #     path('user/<str:pk1>/updateParking/<str:pk2>/',
    #          parkingViews.userUpdateParking, name='userUpdateParking'),
    #     path('getParking/<str:pk>',
    #          parkingViews.getLot, name='getLot'),

    #     # ---LotA-urls---
    path('createLotA/', lotAViews.createLotA, name='createLotA'),

    path('getLotA/', lotAViews.getLotA, name='getLotA'),
    path('updateParkingLotA/<str:pk>',

         lotAViews.updateParkingLotA, name='updateParkingLotA'),
    path('user/<int:pk1>/userGetLotA/',
         lotAViews.userGetLotA, name='userGetLotA'),
    path('user/<int:pk1>/userUpdateParkingLotA/<int:pk2>/',
         lotAViews.userUpdateParkingLotA, name='userUpdateParkingLotA'),
    #     path('getParking/<str:pk>', lotAViews.getLot, name='getLot'),

    #     # ---LotB-urls---
    path('createLotB/', lotBViews.createLotB, name='createLotB'),

    path('getLotB/', lotBViews.getLotB, name='getLotB'),
    path('updateParkingLotB/<str:pk>',

 
         lotBViews.updateParkingLotB, name='updateParkingLotB'),
    path('user/<int:pk1>/userGetLotB/',
         lotBViews.userGetLotB, name='userGetLotB'),
    path('user/<int:pk1>/userUpdateParkingLotB/<int:pk2>/',
         lotBViews.userUpdateParkingLotB, name='userUpdateParkingLotB'),

    #     # ---LotC-urls---
    path('createLotC/', lotCViews.createLotC, name='createLotC'),

    path('getLotC/>', lotCViews.getLotC, name='getLotC'),
    path('updateParkingLotC/<str:pk>',

         lotCViews.updateParkingLotC, name='updateParkingLotC'),
    path('user/<int:pk1>/userGetLotC/',
         lotCViews.userGetLotC, name='userGetLotC'),
    path('user/<int:pk1>/userUpdateParkingLotC/<int:pk2>/',
         lotCViews.userUpdateParkingLotC, name='userUpdateParkingLotC'),

    #     # ---LotD-urls---
    path('createLotD/', lotDViews.createLotD, name='createLotD'),

    path('getLotD/', lotDViews.getLotD, name='getLotD'),
    path('updateParkingLotD/<str:pk>',

         lotDViews.updateParkingLotD, name='updateParkingLotD'),
    path('user/<int:pk1>/userGetLotD/',
         lotDViews.userGetLotD, name='userGetLotD'),
    path('user/<int:pk1>/userUpdateParkingLotD/<int:pk2>/',
         lotDViews.userUpdateParkingLotD, name='userUpdateParkingLotD'),

    # ---message-urls---
    path('createMessage/', messageViews.createMessage, name='createMessage'),
    path('getMessage/<int:pk>', messageViews.getMessage, name='getMessage'),
    path('updateMessage/<int:pk>', messageViews.updateMessage, name='updateMessage')

