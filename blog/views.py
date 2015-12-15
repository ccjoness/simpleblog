from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Post

from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def post_list(request):
    posts = Post.objects.all()
    context_dict = {'posts': posts}
    return render(request, 'post_list.html', context_dict)


def post_view(request, cat, slug):
    post = Post.objects.get(slug=slug)
    context_dict = {'post': post}
    return render(request, 'post.html', context_dict)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'slug', 'text', 'image']
    template_name = 'edit_post.html'
    success_url = '/blog/'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'text', 'image']
    success_url = '/blog/'
    template_name = 'post_new.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        form.instance.slug = form.instance.title.replace(' ', '-').lower()
        return super(CreatePost, self).form_valid(form)


class DeletePost(DeleteView):
    model = Post
    success_url = '/blog/'
    template_name = 'confirm_delete.html'
