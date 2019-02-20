from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from plantmateApp import views

urlpatterns = [url(r'^$', views.home, name='home'),
               url(r'^$', include('plantmateApp.urls')),
               url(r'^admin/', admin.site.urls),
               ]

