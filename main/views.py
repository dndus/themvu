from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


class MainIndex(ListView):
    template_name = 'main/index.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_posts'] = Post.objects.order_by('-id')[:3]
        context['recommend'] = Post.objects.order_by('?')[:1]
        return context
