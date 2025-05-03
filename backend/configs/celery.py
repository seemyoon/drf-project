import os

from celery import Celery

os.environ.setdefault('DJANGO.SETTINGS_MODULE', 'configs.settings')
# it means if we don't this line 'DJANGO.SETTINGS_MODULE', 'configs.settings' then he will put it. so that redis know where configuration is
app = Celery('settings')
# ... continue
