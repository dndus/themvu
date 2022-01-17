from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from .forms import *


class ClientProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'photo']
    template_name = 'layouts/form.html'
    success_url = reverse_lazy('profile')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.page_title = _("Profile")
        request.button_title = _("Saqlash")

    def get_object(self, queryset=None):
        return self.request.user


def account_registration(request):
    if request.user.is_authenticated:
        return redirect('index')

    request.button_title = _('Registration')
    request.page_title = request.button_title
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            return redirect('index')
    return render(request, "account/registration.html", {
        'form': form
    })


def account_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = LoginForm()
    request.button_title = request.page_title = _('Login')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')

    return render(request, 'account/login.html', {
        'form': form
    })


def account_logout(request):
    if not request.user.is_authenticated:
        return redirect('index')

    logout(request)
    return redirect('index')