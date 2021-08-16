from django.urls import path 
from . import views

urlpatterns=[
    path('shows',views.index),
    path('shows/new',views.new_show),
    path('shows/add',views.tv_show),
    path('shows/<int:id>/update',views.update_show),
    path('shows/<int:id>',views.show_shows_id),
    path('shows/<int:id>/edit',views.edit_shows_id),
    path('shows/<int:id>/destroy',views.delete),
]