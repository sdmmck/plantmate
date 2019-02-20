from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quiz', views.quiz, name='quiz'),
    url(r'^recommendations/', views.recommendations, name='recommendations'),
    url(r'^$', views.login, name='login'),
    url(r'^$', views.signup, name='signup'),
    url(r'^plant/', views.plant, name='plant'),
    #url(r'^plant-list/', views.plantList, name='plantList'),
    url(r'^business-list/$', views.businesslist, name='business-list'),
    url(r'^business-list/business/$', views.show_business, name='show_business'),
    url(r'^add_business/$', views.add_business, name='add_business'),
    url(r'^plant/', views.plant, name='plant'),
    url(r'^plant-list/', views.plant_list, name='plant_list'),
    url(r'^myaccount/wishlist/', views.wishlist, name='wishlist'),
    url(r'^myaccount/my-plants/', views.my_plants, name='my_plants'),
]
