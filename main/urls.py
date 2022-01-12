from django import urls
from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name='index')
]