from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^sign-up/', views.signup, name='signup'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^quiz/', views.quiz, name='quiz'),
    url(r'^recommendations/', views.recommendations, name='recommendations'),
    url(r'^business-list/$', views.businesslist, name='business-list'),
    url(r'^add-business/$', views.add_business, name='add_business'),
    url(r'^plant-list/plant', views.plant, name='plant'),
    url(r'^plant-list/$', views.plant_list, name='plant_list'),
    url(r'^myaccount/wishlist/$', views.wishlist, name='wishlist'),
    url(r'^myaccount/my-plants/$', views.my_plants, name='my_plants'),
    url(r'^register/$', views.register, name='register'),
    url(r'^business-list/(?P<business_name_slug>[\w\-]+)/$',
        views.show_business,
        name='show_business'),
    url(r'^add-plant/$', views.add_plant, name='add_plant'),
]

