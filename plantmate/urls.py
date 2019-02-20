
from django.conf.urls import url, include
from django.contrib import admin
from plantmateApp import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^', include('plantmateApp.urls')),
    url(r'^admin/', admin.site.urls),
]
