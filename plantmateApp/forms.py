from django import forms
from plantmateApp.models import Business, Plant
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


class PlantForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Plant name: ")
    latin_name = forms.CharField(max_length=128,
                           help_text="Please enter the plant's latin name: ")
    plant_size = forms.CharField(max_length=128,
                           help_text="Please enter the size the plant will grow to: ")
    plant_characteristics = forms.Select(choices=(("a","Easy to care for"),("b", "Air purifying"),
                                                  ("c","Trailing/Hanging")))

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Plant
        fields = ('name', 'latin_name',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
