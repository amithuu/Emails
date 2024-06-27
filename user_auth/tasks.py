
from celery import shared_task
from .emails import send_login_email, send_login_credentials
from celery.utils.log import get_task_logger

log = get_task_logger(__name__)

@shared_task(name = 'send_signup_email_task')
def send_signup_email_task(email):
    log.info('Welcome Message Sent!')
    return send_login_email(email)

@shared_task(name = 'send_login_credential')
def send_login_credential(email, username, password):
    log.info('Login credentials sent!')
    return send_login_credentials(email, username, password)


# ? This is how we can schedule task for sending email after registration..
# from datetime import timezone, timedelta
# from user_auth.models import CustomUser
# @shared_task
# def send_email_new_signup():
#     last_time_run = timezone.now() - timedelta(minutes=15)
#     new_users = CustomUser.objects.filter(created_at__gt = last_time_run)
    
#     for user in new_users:
#         send_login_email(user.email)
        
