from django.db import models
from django.utils import timezone

class SoftDeleteMixin(models.Model):
    """
    Mixin para implementar eliminación suave (soft delete)
    """
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True  # Esto hace que sea un modelo abstracto, no se crea tabla para él
    
    def delete(self, using=None, keep_parents=False):
        """
        Sobrescribe el método delete para realizar una eliminación suave
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    def hard_delete(self):
        """
        Eliminación física real del registro
        """
        super().delete()
    
    def restore(self):
        """
        Restaurar un registro previamente eliminado
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()


class SoftDeleteManager(models.Manager):
    """
    Manager personalizado para filtrar objetos no eliminados por defecto
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
    def all_with_deleted(self):
        """
        Retorna todos los objetos, incluyendo los eliminados
        """
        return super().get_queryset()
    
    def only_deleted(self):
        """
        Retorna solo los objetos eliminados
        """
        return super().get_queryset().filter(is_deleted=True)
    
    def restore(self, *args, **kwargs):
        """
        Restaura objetos eliminados
        """
        qs = self.only_deleted()
        if args or kwargs:
            qs = qs.filter(*args, **kwargs)
        qs.update(is_deleted=False, deleted_at=None)

class TimeStampedMixin(models.Model):
    """
    Mixin para agregar campos de timestamp created_at y updated_at
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # Esto hace que sea un modelo abstracto