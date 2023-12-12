from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):

    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to="users/profile_images")

    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)

    def __str__(self):
        return f'User: {self.username}'
