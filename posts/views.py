from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
# from users.models import User
from django.views.generic import ListView, DetailView, CreateView


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        return query.select_related('user')


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'
    paginate_by = 6


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'comments/create_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id)
        context['post'] = post
        return context

    def form_valid(self, form):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id)
        form.instance.post = post
        return super().form_valid(form)


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comments/comment_detail.html'
    context_object_name = 'comment'
