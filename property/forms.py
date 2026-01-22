from django.forms import ModelForm
from .models import propertys, booking
from django import forms


class propertys_form(ModelForm):
    class Meta:
        model = propertys 
        fields = ['name','description','location','capacity','price','property_image','available']
    def __init__(self, *args, ** kwargs):
        super(propertys_form, self).__init__(*args, ** kwargs)
        self.fields['name'].widget.attrs.update({'class': "subscription-input-form ", 'placeholder':"Enter your name here"})
        self.fields['description'].widget.attrs.update({'class': "subscription-input-form input_size",'style':'height: 150px', 'placeholder':"Enter your description here"})
        self.fields['location'].widget.attrs.update({'class': "subscription-input-form ", 'placeholder':"Enter your location here"})
        self.fields['price'].widget.attrs.update({'class': "subscription-input-form ", 'placeholder':"Enter your price here"})
        self.fields['capacity'].widget.attrs.update({'class': "subscription-input-form ", 'placeholder':"Enter your capacity here"})
        self.fields['property_image'].widget.attrs.update({})
        self.fields['available'].widget.attrs.update({'class': "subscription-input-form ", 'placeholder':"Enter your email here"})

class booking_form(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['property', 'date']