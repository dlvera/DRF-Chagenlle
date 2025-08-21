from django.db import models
from django.conf import settings
from app.post.models.SoftDeleteMixin import SoftDeleteMixin, SoftDeleteManager
from app.post.models.TimeStampedMixin import TimeStampedMixin 

class Post(SoftDeleteMixin, TimeStampedMixin, models.Model):  # Agregar TimeStampedMixin
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True, through='PostTags')
    
    # Eliminar los campos created_at y updated_at ya que vienen del mixin
    objects = SoftDeleteManager()
    
    def __str__(self):
        return self.title

# Define el modelo through en el mismo archivo
class PostTags(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'app_post_post_tags'
        unique_together = ['post', 'tag']