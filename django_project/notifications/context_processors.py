# notifications/context_processors.py

from .models import Notification

def notifications(request):
    """
    Context processor that returns unread notifications for the logged-in user.
    """
    if request.user.is_authenticated:
        unread_notifications = Notification.objects.filter(
            recipient=request.user, read=False
        )
        # notifications_unread_count = unread_notifications.count()
        notifications_unread_count = Notification.objects.filter(recipient=request.user, read=False).count()
        user_notifications = unread_notifications[:5]  # Fetch the first 5 unread notifications for dropdown

        return {
            'notifications_unread_count': notifications_unread_count,
            'user_notifications': user_notifications
        }
    return {}
