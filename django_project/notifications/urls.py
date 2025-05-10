# urls.py inside each app

from django.urls import path
from . import views

app_name = 'notifications'  # Enables namespacing

urlpatterns = [

    # Route to view all notifications
    path('', views.notifications_list, name='list'),
    
    # Optionally, if you want to mark notifications as read
    path('mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark-as-read'),
    path('go-to/<int:notification_id>/', views.go_to_notification, name='go-to'),
]
