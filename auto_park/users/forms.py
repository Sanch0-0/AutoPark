from django import forms
from .models import User


class RegisterForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            self.add_error("password2", "Passwords didn't match")

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]

        if User.objects.filter(phone_number=phone_number).exists():
            self.add_error("phone_number", "This phone number is already registered")

        return phone_number


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
