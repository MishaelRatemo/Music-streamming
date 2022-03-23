from django.contrib import admin
from .models import Album, Ratings, Review, Profile, Song, User
 
admin.site.register(Album)
admin.site.register(Ratings)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Song)
