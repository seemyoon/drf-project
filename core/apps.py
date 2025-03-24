from django.apps import AppConfig

# Core is common dir for entire project
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
