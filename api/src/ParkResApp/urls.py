from django.conf.urls import url
from ParkResApp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:pk>', views.getUser, name='getUser'),
    path('updateUser/<str:pk>', views.updateUser, name='updateUser'),
    path('deleteUser/<str:pk>', views.deleteUser, name='deleteUser'),
    path('createUser/', views.createUser, name='createUser')
]
