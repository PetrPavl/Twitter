from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView, login_view, UserLogoutView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('<str:username>/', UserListView.as_view(), name='user_post_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    path('users/register/', UserCreateView.as_view(), name='register_user'),
    path('users/login/', login_view, name='login_view'),
    path('users/logout/', UserLogoutView.as_view(), name='user_logout')
]
