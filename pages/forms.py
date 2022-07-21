from django import forms
from django.db import models
from django.db.models import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Adinizi Daxil Edin'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Soyadinizi Daxil Edin'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder' :'Soyadinizi Daxil Edin'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Nomrenizi Daxil Edin'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder' : 'Buyurun...'
    }))

    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','phone','message']