from django.db import models
from django.conf import settings
from app.common.models import SoftDeleteManager, SoftDeleteMixin, TimeStampedMixin

class Comment(SoftDeleteMixin, TimeStampedMixin, models.Model):  # Agregar TimeStampedMixin
    post = models.ForeignKey('app_post.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    
    # Eliminar los campos created_at y updated_at ya que vienen del mixin
    objects = SoftDeleteManager()
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"