from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator


# Register your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    photo = CloudinaryField('image')    
    fname =models.CharField(max_length=50)
    lname =models.CharField(max_length=50)  
    phone = models.CharField(max_length=16,blank=True)      
    email = models.EmailField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, default="No bio yet", blank=True)
    join_date =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
class Album(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = CloudinaryField('image')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist
    
class Song(models.Model):
    title = models.CharField(max_length=80)
    album_cover = CloudinaryField('image')
    song_item = models.FileField(upload_to='music/')
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save_post(self):
        self.save()
    
class Ratings(models.Model):
    beats = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Review(models.Model):
    comment = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    song_item = models.ForeignKey(Song,on_delete=models.CASCADE)
    commented_on= models.DateTimeField(auto_now_add=True)
    
    def save_comment(self):
        self.save()
    
    @classmethod
    def delete_comment(cls,comment):
        cls.objects.filter(comment=comment).delete()