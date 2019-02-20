from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^plant/', views.plant, name='plant'),
    url(r'^plant-list/', views.plantList, name='plantList')
]
