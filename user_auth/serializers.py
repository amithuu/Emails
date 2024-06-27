from rest_framework import serializers
from .models import CustomUser, UserProfile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=64)
    last_name = serializers.CharField(required=True, max_length=64)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    contact = serializers.CharField(required=True,write_only=True,max_length=20)
    address = serializers.CharField(required=True, max_length=64)
    email = serializers.CharField(required=True, max_length=64,validators=[UniqueValidator(queryset=CustomUser.objects.all(),message=("A user is already registered with this email address."))])
    username = serializers.CharField(required=True, max_length=64, validators=[UniqueValidator(queryset=CustomUser.objects.all(),message=("A user is already registered with this username."))])
    
        
    def validate(self, attrs):
        if attrs['password'] !=  attrs['confirm_password']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        
        del attrs['confirm_password'] # as no need to store confirm password..
        
        return attrs

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','username','email','address']
        


# ? which checks the user username and password.. 
from django.contrib.auth import authenticate
class LoginSerializer(serializers.Serializer):
    username =serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Either email or password is incorrect')



class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('headline','user')
        
