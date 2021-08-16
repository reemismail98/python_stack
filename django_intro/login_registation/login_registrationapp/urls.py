from django.urls import path
from django.urls.conf import include     
from . import views
urlpatterns = [
    path('registration', views.registration),
    path('login', views.login),
    path('', views.index),
    path('success',views.success),

    ]


