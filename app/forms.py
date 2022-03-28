
from .models import Album, Ratings, Review, Profile, Song
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from cloudinary.models import CloudinaryField


class EditProfileForm(UserChangeForm):
    photo = CloudinaryField('image')    

    class Meta:
        model= User        
        fields= (
            'email',
            'first_name',
            'last_name',
            'password',
        )



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


