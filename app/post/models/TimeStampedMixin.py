from django.db import models

class TimeStampedMixin(models.Model):
    """
    Mixin para agregar campos de timestamp created_at y updated_at
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # Esto hace que sea un modelo abstracto