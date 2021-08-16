from django.urls import path
from django.urls.conf import include     
from . import views
urlpatterns = [
    path('registration', views.registration),
    path('login', views.login),
    path('', views.index),
    path('wall',views.success),
    path('logout',views.logout), 
    path('postthemessage',views.postthemessage), 
    path('wallcomment',views.postthecomment),
    path('deletecomment',views.deletecomment),
    ]


