from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^plant/', views.plant, name='plant'),
    url(r'^plant-list/', views.plant_list, name='plant_list'),
    url(r'^myaccount/wishlist/', views.wishlist, name='wishlist'),
    url(r'^myaccount/my-plants/', views.my_plants, name='my_plants'),
]
