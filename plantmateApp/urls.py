from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.quiz, name='quiz'),
    url(r'^$', views.recommendations, name='recommendations'),
    url(r'^$', views.login, name='login'),
    url(r'^$', views.signup, name='signup'),
]
