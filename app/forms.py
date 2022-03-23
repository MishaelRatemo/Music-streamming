from turtle import update
from .models import Album, Ratings, Review, Profile, Song, User
from django import forms

class profileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude= ['user', 'join_date']
class albumForm(forms.ModelForm):
    class  Meta:
        model= Album
        exclude= ['user']

class songForm(forms.ModelForm):
    class  Meta:
        model= Song
        exclude= ['username', 'upload_date']
        
        
class ratingForm(forms.ModelForm):
    class  Meta:
        model= Ratings
        exclude= ['user']
class reviewForm(forms.ModelForm):
    class  Meta:
        model= Review
        fields= ['comment']


