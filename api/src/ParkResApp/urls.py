from django.conf.urls import url
from ParkResApp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:pk>', views.getUser, name='getUser'),
    path('updateUser/<str:pk>', views.updateUser, name='updateUser'),
    path('deleteUser/<str:pk>', views.deleteUser, name='deleteUser'),
    path('createUser/', views.createUser, name='createUser'),

    # ---parking-urls---
    path('createParking/', views.createParking, name='createParking'),
    path('getParking/<int:pk>', views.getParking, name='getParking'),
    path('updateParking/<str:pk>', views.updateParking, name='updateParking'),
    path('user/<str:pk1>/getParking/',
         views.userGetParking, name='userGetParking'),
    path('user/<str:pk1>/updateParking/<str:pk2>/',
         views.userUpdateParking, name='userUpdateParking'),
    path('getParking/<str:pk>',
         views.getLot, name='getLot'),

    # ---message-urls---
    path('createMessage/', views.createMessage, name='createMessage'),
    path('getMessage/<str:pk>', views.getMessage, name='getMessage'),
    path('updateMessage/<str:pk>', views.updateMessage, name='updateMessage')
]
