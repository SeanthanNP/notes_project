from django.db import models
from django.core.exceptions import ValidationError

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Optional: Add custom MongoDB saving logic if needed
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title