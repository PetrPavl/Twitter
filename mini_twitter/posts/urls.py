from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('posts/<int:post_id>/add-comment', views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>', views.comment_detail, name="comment_detail"),
    path('<str:username>/', views.post_list, name='user_post_list'),
    path('posts/add-post', views.add_post, name='add_post'),
    path('posts/<int:post_id>', views.post_detail, name="post_detail")

]
