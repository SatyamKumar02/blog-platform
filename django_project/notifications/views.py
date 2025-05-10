# Create your views here.

# notifications/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

# views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from notifications!")


@login_required
def notifications_list(request):
    # Get all notifications for the logged-in user
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-timestamp')  # Order by most recent
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    # Get the notification object by its ID
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    
    # Mark the notification as read
    notification.read = True
    notification.save()

    # # Redirect back to the notifications list
    # return redirect('notifications-list')

    # Redirect to the notification's URL or a fallback
    return redirect(notification.url or 'blog:post-list')

def go_to_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)

    # Mark as read
    if not notification.read:
        notification.read = True
        notification.save()

    # Redirect to target URL or fallback
    return redirect(notification.url or 'blog:post-list')