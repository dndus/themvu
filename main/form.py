from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'subject_uz', 'subject_en', 'video']