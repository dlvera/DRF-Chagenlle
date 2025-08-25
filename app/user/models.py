from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from app.common.models import SoftDeleteManager, SoftDeleteMixin, TimeStampedMixin

# Agrega un manager personalizado para CustomUser
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener una dirección de correo electrónico')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser, SoftDeleteMixin, TimeStampedMixin):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=True)

    # Usar el nuevo manager personalizado para usuarios
    objects = CustomUserManager()
    
    # Mantén los related_name personalizados para evitar conflictos
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
    
    def __str__(self):
        return self.username

class Profile(SoftDeleteMixin, TimeStampedMixin, models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    
    # Usar el manager personalizado de common para soft delete
    objects = SoftDeleteManager()

    def __str__(self):
        return f'{self.user.username} Profile'