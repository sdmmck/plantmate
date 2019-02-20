from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^plant', views.plant, name='plant'),
]