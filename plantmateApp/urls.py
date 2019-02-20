from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^plant/', views.plant, name='plant'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^myaccount/', views.myaccount, name='myaccount'),

]
