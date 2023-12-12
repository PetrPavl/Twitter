from django.contrib import admin

from users.models import User
from posts.models import Post, Comment

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)


