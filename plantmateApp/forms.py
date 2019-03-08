
from plantmateApp.models import Business, Plant, PlantImage, UserSavedPlants, UserWishlistPlants
from django import forms
from django.contrib.auth.models import User
from plantmateApp.models import UserProfile


class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Business name.")
    address = forms.CharField(max_length=128,
                              help_text="Enter the Business address.")
    postcode = forms.CharField(max_length=8,
                               help_text="Enter the Business postcode.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Business
        fields = ('name','address','postcode')


class PlantForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Plant name: ")
    latin_name = forms.CharField(max_length=128,
                           help_text="Please enter the plant's latin name: ")
    size = forms.ChoiceField(required=False, widget=forms.Select,
                                        help_text="Size this plant will grow to: ",
                                        choices=Plant.size_choices)
    climate = forms.ChoiceField(required=False, widget=forms.Select,
                                        help_text="Does this plant prefer warm or cool rooms? ",
                                        choices=Plant.climate_choices)
    light = forms.ChoiceField(required=False, widget=forms.Select,
                                        help_text="Does this plant like it sunny or shady? ",
                                        choices=Plant.light_choices)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Plant
        fields = ('name', 'latin_name', 'size', 'climate', 'light', 'room')


class ImageForm(forms.ModelForm):

    picture = forms.ImageField(required=False)
    plant_name = forms.HiddenInput()

    class Meta:
        model = PlantImage
        fields = ('picture', 'plant_name')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class SavePlantForm(forms.ModelForm):
    saved_plant = forms.HiddenInput()

    class Meta:
        model = UserSavedPlants
        fields = ('saved_plant',)
        exclude = ('user',)


class WishlistPlantForm(forms.ModelForm):
    wishlist_plant = forms.HiddenInput()

    class Meta:
        model = UserWishlistPlants
        fields = ('wishlist_plant',)
        exclude = ('user',)
