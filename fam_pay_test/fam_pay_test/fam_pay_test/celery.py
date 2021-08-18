import os
from celery import Celery
from . import celery_config
import os
from django.conf import settings

os.environ.setdefault('DJANAGO_SETTINGS_MODULE', 'fam_pay_test.settings')

app = Celery('fam_pay_test')

app.config_from_object(celery_config)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)