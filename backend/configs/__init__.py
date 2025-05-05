from .celery import app as celery_app

__all__ = ['celery_app']
# it means when we relate to package of configs, it can take celery_app at once.
# celery_app for its