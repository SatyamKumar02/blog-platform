from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'verb', 'read', 'timestamp')
    search_fields = ('recipient__username', 'sender__username', 'verb')
    list_filter = ('read', 'timestamp')

admin.site.register(Notification)