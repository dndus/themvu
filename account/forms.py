from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(label=_("Parol takroran"), widget=forms.PasswordInput)

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise  ValidationError(_("Parollar bir xil emas"))

        return  self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password']
        labels = {
            'username': _("Login"),
            'first_name': _("Ism"),
            'last_name': _("Falimiliya"),
            'email': _("E-mail"),
            'password': _("Parol")
        }

        widgets = {
            'password': forms.PasswordInput
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)
