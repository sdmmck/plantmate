from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quiz/', views.quiz, name='quiz'),
    url(r'^recommendations/', views.recommendations, name='recommendations'),
    url(r'^$', views.login, name='login'),
    url(r'^$', views.signup, name='signup'),
    url(r'^plant/', views.plant, name='plant'),
    url(r'^plant-list/', views.plantList, name='plantList'),
]
