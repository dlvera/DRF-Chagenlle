from django.db import models
from django.contrib.auth.models import AbstractUser
from app.post.models.SoftDeleteMixin import SoftDeleteMixin, SoftDeleteManager
from app.post.models.TimeStampedMixin import TimeStampedMixin  

class CustomUser(AbstractUser, SoftDeleteMixin, TimeStampedMixin):  # Agregar TimeStampedMixin
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=True)

    # Es crucial definir related_name únicos para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions_set",
        related_query_name="customuser",
    )
    
    # Usar el manager personalizado
    objects = SoftDeleteManager()
    
    def __str__(self):
        return self.username
class Profile(SoftDeleteMixin, TimeStampedMixin, models.Model):  # Agregar TimeStampedMixin
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    
    # Usar el manager personalizado
    objects = SoftDeleteManager()

    def __str__(self):
        return f'{self.user.username} Profile'