from django.urls import path
from django.urls.conf import include     
from . import views
urlpatterns = [
    path('registration', views.registration),
    path('login', views.login),
    path('', views.index),
    path('thoughts',views.success),
    path('logout', views.logout),
    path('postthethought',views.postthethought),
    path('deletethought',views.deletethought),
    path('thoughts/<int:id>',views.detalies),
    path('thoughts/addliked/<int:id>',views.addthought),
    path('thoughts/removeliked/<int:id>',views.removethought),
    ]


