from django.db import models
from app.user.models import SoftDeleteMixin, SoftDeleteManager 

class Tag(SoftDeleteMixin, models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Usar el manager personalizado
    objects = SoftDeleteManager()

    def __str__(self):
        return self.name