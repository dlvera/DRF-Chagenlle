from django.db import models
from django.conf import settings
from app.post.models.SoftDeleteMixin import SoftDeleteMixin, SoftDeleteManager 

class Post(SoftDeleteMixin, models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True, through='PostTags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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