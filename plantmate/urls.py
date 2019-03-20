from django.conf.urls import url, include
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from plantmateApp import views


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '^$'
    # currently does not work. trying to redirect to home.


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^', include('plantmateApp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
]
