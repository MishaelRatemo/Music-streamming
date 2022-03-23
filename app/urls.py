from django.urls import  path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
     # API VIWS Get
    path('getalbums/', views.get_album),
    path('getprofiles/', views.get_profiles),
    path('getratings/', views.get_ratings),
    path('getreviews/', views.get_reviews),
    # API view POST
    path('addrate/', views.add_rate)
    
]