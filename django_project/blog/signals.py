from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from notifications.models import Notification
from django.urls import reverse

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
