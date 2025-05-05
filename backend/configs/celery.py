import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
# it means if we don't this line 'DJANGO.SETTINGS_MODULE', 'configs.settings' then he will put it. so that redis know where configuration is
app = Celery('settings')  # standard settings
# configuration

app.config_from_object('django.conf:settings', namespace='CELERY')

# -----cron settings--------
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_spam_every_minutes': {
        'task': 'core.services.email_service.spam',  # path to task where will be occurred
        'schedule': crontab()
        # 'args':() - use we if we have arguments and in specific order specify it
    }
    # send_spam_every_minutes is arbitrary name
}
