
from plantmateApp.models import Business, Plant, PlantImage, UserSavedPlants, UserWishlistPlants, Comment
from django import forms
from django.contrib.auth.models import User
from plantmateApp.models import UserProfile


class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Business name.")
    address = forms.CharField(max_length=128,
                              help_text="Enter the Business address.")
    lat = forms.CharField(widget=forms.HiddenInput(), required=True)
    long = forms.CharField(widget=forms.HiddenInput(), required=True)
    url = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    opening_hours = forms.CharField(required=False)

    class Meta:

        model = Business
        fields = ('name', 'address', 'lat', 'long', 'phone', 'email', 'opening_hours', 'url')


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
    picture = forms.ImageField(required=False)

    class Meta:

        model = Plant
        fields = ('name', 'latin_name', 'size', 'climate', 'light', 'room', 'picture')


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


class ProfileImageForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture',)


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


class CommentForm(forms.ModelForm):
    plant_slug = forms.HiddenInput()
    body = forms.Textarea()

    class Meta:
        model = Comment
        fields = ('plant_slug', 'body', )
        exclude = ('approved_comment', )


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
