from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'age', 'phone_number', 'email', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }