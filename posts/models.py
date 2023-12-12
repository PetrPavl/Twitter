from django.db import models
from django.urls import reverse
from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'             # в адмінці
        verbose_name_plural = 'Пости'
        ordering = ['title']

    def __str__(self):
        return f'Post: {self.title}, {self.user}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.pk})
