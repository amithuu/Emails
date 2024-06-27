from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=10)
    
    # first_name = models.CharField(max_length=10)  
    # last_name = models.CharField(max_length=10)
    # * as we get first_name, last_name and username all form {AbstractUser Model itself}, so we are not adding to models directly
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    # * we need to initialize this as when this model is created it by defaults calls that manager instance.. and runs create_user and createsuperuser function based on called function..
    objects = CustomUserManager() 
    
    class Meta:
        db_table = 'users'
    
        
    def __str__(self):
        return self.username


from django.conf import settings
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'profiles'
        
    def __str__(self):
        return self.user.username


