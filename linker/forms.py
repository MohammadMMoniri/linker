from django import forms
from .models import LinkModel

URL_REGEX = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


class AnonymousLinkForm(forms.ModelForm):
    link = forms.RegexField(regex=URL_REGEX, widget=forms.TextInput(attrs={'class' : 'form-control', "aria-describedby":"button-addon2"}))

    class Meta:
        model = LinkModel
        fields = ["link"]
        fields_required = ['link']

