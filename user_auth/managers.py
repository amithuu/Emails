
# * As We are Overriding the default User MODEls, so we need to write this CustomUSer manager which manages the USer models..


# When we use User Model, by default it will call createUser and createsuperuser function.. that we need to define explicitly here 

from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):  # for making the email_normalize we use BaseUserManager..
    
    def create_user(self,username,password, **extra_fields):
        if not username:
            raise ValueError('User must have an username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUSer must have is_staff and is_superuser to True')
        return self.create_user(username, password, **extra_fields)
    
    
        
        
    
    
    