from django.conf.urls import url
from django.urls import path
from .views import*
urlpatterns =[
    url('',home, name="home"),
    url('Register/', Register,name="Register"),
    url('login/', login, name='login'),
]
