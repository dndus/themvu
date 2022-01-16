from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .forms import *


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