from django.db import models
from app.common.models import SoftDeleteManager, SoftDeleteMixin, TimeStampedMixin

class Tag(SoftDeleteMixin, TimeStampedMixin, models.Model):  # Agregar TimeStampedMixin
    name = models.CharField(max_length=50, unique=True)
    
    # Eliminar el campo created_at ya que viene del mixin
    objects = SoftDeleteManager()

    def __str__(self):
        return self.name