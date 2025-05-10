from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField

# This model is for a blog post with a title, content, and a ForeignKey relationship to the custom user model.
class Post(models.Model):
    title = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'