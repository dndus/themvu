from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('view/<int:id>/', main_view_post, name="view"),
    path('posts/<int:id>/', all_posts, name='posts'),
    path('posts/', all_posts, name='posts'),
    path('add-post/', main_add_post, name='add-post'),
    path('searched/', main_search, name='searched'),
]