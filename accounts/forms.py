from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TaiKhoan

class TaiKhoanCreationForm(UserCreationForm):
    class Meta:
        model = TaiKhoan
        fields = ['username', 'email', 'password1', 'password2', 'sdt', 'dia_chi']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = TaiKhoan
        fields = ['email', 'sdt', 'dia_chi']  # Only include fields that exist on TaiKhoan

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)