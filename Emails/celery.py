import os 
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Emails.settings')

app = Celery('Emails')

app.config_from_object("django.conf:settings", namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



# ? We can sue this like instead of sending the email every time a user signs-up, we can make task so that for every 30 min it will check that any user has signed in or not
# ? if any user is signed in then we can send mail for that use. 

# app.conf.beat_schedule  = {
#     'SCHEDULE_TASK':{
#         'task':'user_auth.tasks.send_login_email_task',
#         'schedule':crontab(minute='*/30'), # for every 30 min this will execute..
#     }
# }