from django.urls import  path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/song', views.song_post, name='new_song'),
    path('profile',views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    
    path('logout', views.logout, name='logout'),
    
    
     # API VIWS Get
    path('getalbums/', views.get_album),
    path('getprofiles/', views.get_profiles),
    path('getratings/', views.get_ratings),
    path('getreviews/', views.get_reviews),
    # API view POST
    path('addrate/', views.add_rate)
    
]