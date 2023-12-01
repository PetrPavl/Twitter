from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('<str:username>/', views.user_list, name='user_post_list'),
    path('users/<int:user_id>', views.user_detail, name="user_detail"),
    #path('users/add-user', views.add_user, name='add_user'),
]
