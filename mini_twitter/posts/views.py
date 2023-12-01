from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from users.models import User


def post_list(request, username=None):
    user = None
    if username:
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(user=user)
    else:
        posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts, 'user': user})


def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments/comment_list.html', {'comments': comments})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "posts/post_detail.html", context)


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user_id = request.user.id
            comment.save()
            return redirect('comment_detail', comment_id=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'comments/create_comment.html', {'form': form, 'post': post})


def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    context = {"comment": comment}
    return render(request, "comments/comment_detail.html", context)
