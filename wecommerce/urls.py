from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    
    
    path(r'',views.login,name="login"),
  
]