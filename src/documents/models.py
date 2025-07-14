from django.conf import settings
from django.db import models
from django.utils import timezone


# Auth User
User = settings.AUTH_USER_MODEL


# Document DB model
class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default="Title")
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if self.active and self.active_at is None:
            self.active_at = timezone.now()
        else:
            self.active_at = None

        return super().save(*args, **kwargs)
