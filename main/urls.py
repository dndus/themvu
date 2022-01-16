from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('view/<int:id>/', main_view_post, name="view"),
    path('posts/<int:id>/', all_posts, name='posts')
]