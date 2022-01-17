from django import forms
from django.core.exceptions import ValidationError
from .models import User


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(label="Parol takroran", widget=forms.PasswordInput)

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas")

        return self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

        labels = {
            'username': 'Username'
        }

        widgets = {
            'password': forms.PasswordInput
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)