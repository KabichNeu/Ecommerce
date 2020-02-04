from django import forms
from django.core import validators
from django.contrib.auth.models import User
from registration.models import UserProfileInfo 

class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    verify_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    botcatcher = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators =[validators.MaxLengthValidator(0)]
                                )