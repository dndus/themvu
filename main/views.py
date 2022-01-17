from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.utils.translation import gettext_lazy as _

from .form import PostForm
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


def main_add_post(request):

    if not request.user.is_authenticated:
        return redirect('index')

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            return redirect('main:index')

    request.page_title = _("Maqola qo'shish")
    return render(request, 'main/add-post.html', {
        'form': form
    })


def main_search(request):
    if request.method == 'POST':
        q = request.POST['q']
        post = Post.objects.filter(subject_uz__icontains=q)

        return render(request, 'main/post-search.html', {
            'q': q,
            'posts': post
        })
    else:
        return render(request, 'main/post-search.html', {
        })