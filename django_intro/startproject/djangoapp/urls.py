# from django.urls import path     
# from . import views

# urlpatterns = [
#         path('blog', views.one_method),
#         path('bears/<int:my_val>', views.another_method),
#         path('bears/<str:name>/poke', views.yet_another),
#     	path('<int:id>/<str:color>', views.one_more),
# ]

# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),
    
# ]

from django.urls import path
from . import views
urlpatterns = [
    path('blogs', views.root),
    path('new', views.index),
    path('blogs/new', views.new),
    path('index', views.index),
    path('blogs/create', views.create),
    path('blogs/<number>', views.create),
    path('blogs/<number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('',views.emptyroot)
]