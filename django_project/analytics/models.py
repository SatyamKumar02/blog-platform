from django.db import models

# This model will track page views, capturing the url and the timestamp of each view.
class PageView(models.Model):
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Page view for {self.url} at {self.timestamp}"
