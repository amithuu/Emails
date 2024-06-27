from rest_framework.response import Response 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.generics import *
from .tasks import send_signup_email_task, send_login_credential
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated

class UserRegisterAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny,]
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = CustomUser.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return Response({'Data': serializer.data})
        except Exception as e:
            return Response({'Error':str(e)})
    
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            with transaction.atomic():
                user = CustomUser.objects.create_user(**validated_data)
            
            token = RefreshToken.for_user(user)

            send_signup_email_task.delay(email = user.email)
            
            data = {}
            data['id'] =user.id
            data['username'] = user.username
            data['email'] = user.email
            data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
            }
            return Response({'Data': data})
        
        except Exception as e:
            return Response({'error': str(e)})


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny,]
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = RefreshToken.for_user(user)
        data = {
            'id':user.id,
            'username':user.username,
            'refresh_token':str(token),
            'access_token':str(token.access_token),
        }

        send_login_credential.delay(email=user.email,username = user.username, password = request.data.get('password'))
        return Response({'Data':data, 'success':True})
    

from user_auth.models import UserProfile
from user_auth.serializers import UserProfileSerializer

class UserProfileAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        return self.request.user.userprofile# instead the get method we can write this as well..
    
    # def get(self, request, *args, **kwargs):
    #     serializer =self.get_serializer(self.queryset.filter(user=request.user),many=True)
    #     return Response({'data':serializer.data})
    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({'data':serializer.data})
    



# this is for middleware functionality..
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'index.html',{
        'title':'this is test middleware' 
    })
