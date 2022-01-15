from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


class MainIndex(ListView):
    template_name = 'main/index.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['postall'] = Post.objects.all()
        context['last_posts'] = Post.objects.order_by('-id')[:3]
        context['recommendfy'] = Post.objects.order_by('?')[:6]
        context['recommend'] = Post.objects.order_by('?')[:1]
        context['trending'] = Post.objects.order_by('-view')[:6]
        return context
