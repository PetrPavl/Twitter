from django.urls import path
from . import views
from .views import PostListView, CommentListView, PostDetailView, CommentDetailView, PostCreateView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('posts/<int:pk>/add-comment/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('<str:username>/', PostListView.as_view(), name='user_post_list'),
    path('posts/add-post/', PostCreateView.as_view(), name='add_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
