from django.conf.urls import url,include
from Blogapp import views
urlpatterns =[
    url('Blogapp',views.home, name="home"),
    url('Register/', views.Register,name="Register"),
    url('login/', views.login, name='login'),
]
