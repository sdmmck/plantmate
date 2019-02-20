from django import forms
from plantmateApp.models import Business


class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the Business name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Business
        fields = ('name',)
