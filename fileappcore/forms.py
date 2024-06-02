from django import forms
from django.forms import ModelForm
from .models import User

colors = [
    ('red', 'Red'),
    ('green', 'Green'),
    ('blue', 'Blue'),
]

country = [
    ('india', 'India'),
    ('usa', 'USA'),
    ('uk', 'UK'),
    ('australia', 'Australia'),
    ('japan', 'Japan'),
    ('china', 'China'),
    ('russia', 'Russia'),
    ('canada', 'Canada'),
    ('france', 'France'),
    ('germany', 'Germany'),
    ('spain', 'Spain'),
    ('italy', 'Italy'),
    ('austria', 'Austria'),
    ('ukraine', 'Ukraine'),
    ('poland', 'Poland'),
    ('belgium', 'Belgium'),
]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'country', 'password', 'profile_pic', 'resume', 'mobile_No', 'favorite_color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'country': forms.Select(choices=country, attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'mobile_No': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'favorite_color': forms.Select(choices=colors, attrs={'class': 'form-control'}),
        }