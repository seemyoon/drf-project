CELERY_BROKER_URL = 'redis://redis:6379/0'
# 0 - is bd (it can be about 15 items)
CELERY_RESULTS_BACKEND = 'django-db'
# django-db responsible for results
CELERY_ACCEPT_CONTENT = ['application/json']
# communicate with application/json
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# tasks and serializers will write via json

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'