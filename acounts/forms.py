from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = {'image'}




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'İsdifadəçi adı'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parola'
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Adınızı daxil edin'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Soyadınızı daxil edin'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'İsdifadəçi adı'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-poçt adressi'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parola'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Təkrar Parola'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']





""" from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Phone'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Contact
        fields =  ['first_name', 'last_name', 'email', 'phone', 'message'] """