"""Emails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from email_sending import views
from email_sending.mailtrap import simple

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email',views.simple_email),
    path('email_message',views.email_message),
    path('multi',views.multi),
    path('mass',views.mass),
    path('html',views.html),
    path('attach',views.attach),
    path('simple',simple),
    path('', include('user_auth.urls')),
]
