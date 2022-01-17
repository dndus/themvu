from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', account_registration, name='registration'),
    path('login/', account_login, name='login'),
    path('logout/', account_logout, name='logout'),
    path('profile/', ClientProfile.as_view(), name='profile')
]