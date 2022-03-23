
from rest_framework import serializers
from .models import Album, Ratings, Review, Profile, Song, User


class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model= Album
        fields=['user', 'artist', 'album_title', 'genre', 'album_logo', 'is_favorite']

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields='__all__'
        
        
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__' 
          
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__' 