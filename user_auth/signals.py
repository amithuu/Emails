from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# from user_auth.tasks import send_login_credential
# from django.contrib.auth.signals import user_logged_in

from user_auth.models import UserProfile, CustomUser



@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()  # userprofile is model name here..


@receiver(post_save, sender=CustomUser)
def update_profile(sender, instance, created,**kwargs):
    try:
        if created == False:
            instance.userprofile.save()      
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance.user)



# ? trying to send email when user logs in:
# @receiver(post_save, sender=User)
# @receiver(user_logged_in, sender=User)
# def send_user_login_credentials(sender, instance,created,**kwargs):
#     send_login_credential.delay(email=instance.email,username = instance.username)