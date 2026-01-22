from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import service_provider
from django import forms
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','last_name','email','username','password1','password2']
    def __init__(self, *args, ** kwargs):
        super(CustomUserCreationForm, self).__init__(*args, ** kwargs)
        self.fields['first_name'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your first name here"})
        self.fields['last_name'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your last name here"})
        self.fields['email'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your email here"})
        self.fields['username'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your username here"})
        self.fields['password1'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your password here"})
        self.fields['password2'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"tha same password"})



class edit_profile_form(ModelForm):
    class Meta:
        model = service_provider
        fields = ['name','phone','service_provider_image','short_intro','bio','experience_years','status']
    def __init__(self, *args, ** kwargs):
        super(edit_profile_form, self).__init__(*args, ** kwargs)
        self.fields['name'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your first name here"})
        self.fields['phone'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your phone number here"})
        self.fields['service_provider_image'].widget.attrs.update({'class': "", 'placeholder':"Enter your image here"})
        self.fields['short_intro'].widget.attrs.update({'class': "subscription-input-form margin_input input_h",'style':'height: 150px;', 'placeholder':"Enter your intro here"})
        self.fields['bio'].widget.attrs.update({'class': "subscription-input-form margin_input input_h",'style':'height: 150px;', 'placeholder':"Enter your bio here"})
        self.fields['experience_years'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your experience years here"})
        self.fields['status'].widget.attrs.update({'class': "subscription-input-form margin_input", 'placeholder':"Enter your statusstatus here"})

