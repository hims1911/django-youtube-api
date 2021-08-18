from celery.schedules import crontab
from django.conf import settings

broker_url = settings.BROKER_URL
accept_content = ['json']

beat_schedule = {
        'fetch_video_data': {
            'task': 'fam_pay_main.tasks.fetch_youtube_data',
            'schedule': crontab(minute='*/1')
        }
    }