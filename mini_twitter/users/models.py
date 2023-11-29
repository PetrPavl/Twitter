from django.db import models


class User(models.Model):

    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to="users/profile_images")

    def __str__(self):
        return f'User: {self.username}'
