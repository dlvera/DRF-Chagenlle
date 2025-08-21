from django.db import models
from django.conf import settings  # Importar settings para usar AUTH_USER_MODEL
from app.post.models.SoftDeleteMixin import SoftDeleteMixin, SoftDeleteManager 

class Comment(SoftDeleteMixin, models.Model):
    post = models.ForeignKey('app_post.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Usar el manager personalizado
    objects = SoftDeleteManager()
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"