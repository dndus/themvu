from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.translation import gettext_lazy as _
from .models import *


class MainIndex(ListView):
    request.page_title = _('Bosh sahifa')

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


def main_view_post(request, id):
    post = Post.objects.get(id=id)
    post.view += 1
    post.save()

    request.page_title = post.subject

    request.breadcrumb = [
        post.subject
    ]

    return render(request, 'main/view.html', {
        'post': post,
        'posts': Post.objects.order_by("?")[:3],
        'random': Post.objects.order_by("?")[:5]
    })


def all_posts(request, id=None):
    if id is not None:
        post = Post.objects.get(id=id)
    else:
        post = Post.objects.order_by('-id')
    return render(request, 'main/all-posts.html', {
        'post': post

    })