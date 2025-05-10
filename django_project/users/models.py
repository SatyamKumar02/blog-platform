from django.db import models
from django.contrib.auth.models import AbstractUser

# This will extend Django's default User model and allow for extra fields like bio and profile_picture.
# Custom user model to extend Django's User model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changed related_name to 'customuser_set'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Changed related_name to 'customuser_set'
        blank=True
    )

    def __str__(self):
        return self.username
