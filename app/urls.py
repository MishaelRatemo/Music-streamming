from django.urls import  path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('post/song', views.song_post, name='new_song'),
    path('profile',views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('change-password', views.change_password, name='change_password'),
    path('reset-password', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confrim', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    


    
    path('logout', views.logout, name='logout'),
    
    
     # API VIWS Get
    path('getalbums/', views.get_album),
    path('getprofiles/', views.get_profiles),
    path('getratings/', views.get_ratings),
    path('getreviews/', views.get_reviews),
    # API view POST
    path('addrate/', views.add_rate)
    
]