from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('authors',views.indexauthor),
    path('bookadd',views.bookform),
    path('authors/authorsadd',views.authorform),
    path('books/<int:id>',views.show),
    path('authors/<int:id>',views.showauthor),
    path('selectauthor',views.selectauthor),
    path('selectbook',views.selectbook),
]