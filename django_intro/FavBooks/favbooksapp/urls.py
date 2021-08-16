from django.urls import path
from django.urls.conf import include     
from . import views
urlpatterns = [
    path('registration', views.registration),
    path('login', views.login),
    path('', views.index),
    path('books',views.books),
    path('logout',views.logout), 
    path('addbook',views.addbook),
    path('fav/<int:idu>/<int:idb>',views.favbook),
    path('books/<int:id>',views.showbook),
    path('books/<int:book_id>/remove_from_fav',views.remove_from_fav),
    path('books/<int:book_id>/add_to_fav',views.add_to_fav),]


