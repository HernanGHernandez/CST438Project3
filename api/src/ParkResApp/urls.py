from django.conf.urls import url
from ParkResApp import views

urlpatterns = [
    url(r'^user$', views.userApi),
    url(r'^user/([0-9]+)$', views.userApi)
]
