from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^business-list/$', views.businesslist, name='business-list'),
    url(r'^business-list/business/$', views.show_business, name='show_business'),
    url(r'^add_business/$', views.add_business, name='add_business'),
]
