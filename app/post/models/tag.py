from django.db import models
from app.post.models.SoftDeleteMixin import SoftDeleteMixin, SoftDeleteManager 
from app.post.models.TimeStampedMixin import TimeStampedMixin  # Importar el nuevo mixin

class Tag(SoftDeleteMixin, TimeStampedMixin, models.Model):  # Agregar TimeStampedMixin
    name = models.CharField(max_length=50, unique=True)
    
    # Eliminar el campo created_at ya que viene del mixin
    objects = SoftDeleteManager()

    def __str__(self):
        return self.name