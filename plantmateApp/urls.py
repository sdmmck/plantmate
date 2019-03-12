from django.conf.urls import url
from plantmateApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^login/', views.login, name='login'),
    url(r'^sign-up/', views.signup, name='signup'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^quiz/$', views.quiz, name='quiz'),
    url(r'^business-list/$', views.businesslist, name='business-list'),
    url(r'^add-business/$', views.add_business, name='add_business'),
    url(r'^plant-list/(?P<plant_name_slug>[\w\-]+)/$', views.show_plant, name='plant'),
    url(r'^plant-list/(?P<plant_name_slug>[\w\-]+)/add-image', views.add_image, name='add_image'),
    url(r'^plant-list/$', views.plant_list, name='plant_list'),
    url(r'^myaccount/wishlist/$', views.wishlist, name='wishlist'),
    url(r'^myaccount/my-plants/$', views.my_plants, name='my_plants'),
    url(r'^register/$', views.register, name='register'),
    url(r'^business-list/(?P<business_name_slug>[\w\-]+)/$',
        views.show_business,
        name='show_business'),
    url(r'^add-plant/$', views.add_plant, name='add_plant'),
    url(r'^save-plant/$', views.save_plant, name='save_plant'),
    url(r'^wishlist-plant/$', views.wishlist_plant, name='wishlist_plant'),
    url(r'^add-comment/$', views.add_comment, name='add_comment'),
    url(r'^remove-wishlist-plant/$', views.remove_wishlist_plant, name='remove_wishlist_plant'),
    url(r'^remove-saved-plant/$', views.remove_saved_plant, name='remove_saved_plant'),
    url(r'^quiz/your-plantmate/', views.your_plantmate, name='your_plantmate'),


]
