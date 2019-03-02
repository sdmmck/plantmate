from django import forms
from plantmateApp.models import Business
from django import forms
from django.contrib.auth.models import User
from plantmateApp.models import UserProfile


class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Business name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Business
        fields = ('name',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
