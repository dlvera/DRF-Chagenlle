from django.db import models
from django.conf import settings  # Importar settings para usar AUTH_USER_MODEL
from app.user.models import SoftDeleteMixin, SoftDeleteManager 

class Post(SoftDeleteMixin, models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('post.Tag', related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Usar el manager personalizado
    objects = SoftDeleteManager()
    def __str__(self):
        return self.title