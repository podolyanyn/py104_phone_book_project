from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number')
    name = forms.CharField(label='Name')
    surname = forms.CharField(label='Surname', required=False)
    locality = forms.CharField(label='Locality', required=False)
    email = forms.EmailField(label='Email', required=False)
    social_media = forms.CharField(label='Social Media', required=False)
    black_list_status = forms.BooleanField(label='Blacklist Status', required=False)

    class Meta:
        model = Contact
        fields = ['phone_number', 'name', 'surname', 'locality', 'email', 'social_media', 'black_list_status']
