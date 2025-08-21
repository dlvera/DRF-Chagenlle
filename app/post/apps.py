from django.apps import AppConfig

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.post'
    label = 'app_post'  # Opcional pero recomendado para evitar conflictos