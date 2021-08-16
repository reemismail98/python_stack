from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('dojoform',views.dojoform),
    path('ninjaform',views.ninjaform)
]