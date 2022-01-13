from django.contrib import admin
from .models import *


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'subject_uz',
        'user',
        'category'
    ]
    fields = ('category', 'subject_uz', 'subject_en', 'video')
    search_fields = ['subject_uz']
    list_filter = ['added_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz',
        'name_en'
    ]
