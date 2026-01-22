from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import client
from django import forms
from django.contrib.auth.models import User, Group
from property.models import booking


class client_register_form(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','last_name','email','username','password1','password2']
    def __init__(self, *args, ** kwargs):
        super(client_register_form, self).__init__(*args, ** kwargs)
        self.fields['first_name'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your first name here"})
        self.fields['last_name'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your last name here"})
        self.fields['email'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your email here"})
        self.fields['username'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your username here"})
        self.fields['password1'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your password here"})
        self.fields['password2'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"tha same password"})



class edit_profile_form_client(ModelForm):
    class Meta:
        model = client
        fields = ['username','phone','client_image','birth_date','gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, ** kwargs):
        super(edit_profile_form_client, self).__init__(*args, ** kwargs)
        self.fields['username'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your first name here"})
        self.fields['phone'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your phone number here"})
        self.fields['client_image'].widget.attrs.update({'class': "", 'placeholder':"Enter your image here"})
        self.fields['birth_date'].widget.attrs.update({'class': "subscription-input-form margin_input pading_right" , 'placeholder':"Enter your birth date here"})
        self.fields['gender'].widget.attrs.update({'class': "subscription-input-form margin_input pading_right", 'placeholder':"Enter your gender here"})

class booking_form(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['property', 'date']