from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from .models import Post
from .forms import CommentForm
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-date']
    paginate_by = 10


class UserPostList(ListView):
    model = Post
    template_name = 'blog/userpost.html'
    context_object_name = 'blog_posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetail(LoginRequiredMixin, DetailView, FormMixin):
    model = Post
    template_name = 'blog/detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetail, self).form_valid(form)


class CreatePost(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create.html'
    permission_required = ('')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class DeletePost(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class SearchView(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(author__username__contains=query))
        return object_list

















