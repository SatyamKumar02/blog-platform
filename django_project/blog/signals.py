from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Post
from notifications.models import Notification
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Comment)
def notify_on_comment(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if post.author != instance.author:
            notification_url = reverse('blog:post-detail', kwargs={'pk': post.pk})
            Notification.objects.create(
                recipient=post.author,
                sender=instance.author,
                verb=f"{instance.author.username} commented on your post: '{post.title}'",
                url=notification_url
            )

@receiver(post_save, sender=Post)
def notify_users_on_new_post(sender, instance, created, **kwargs):
    if created:
        author = instance.author
        # Notify all users except the one who posted
        recipients = User.objects.exclude(id=instance.author.id)
        for user in recipients:
            Notification.objects.create(
                sender=author,
                recipient=user,
                verb=f"{instance.author.username} posted a new blog: {instance.title}",
                url=reverse('blog:post-detail', args=[instance.pk])
            )