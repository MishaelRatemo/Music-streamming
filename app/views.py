from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
    
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import  logout as auth_logout
from django.contrib import messages

from app.forms import EditProfileForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Album, Ratings, Review, Profile, Song, User
from .forms import profileForm,albumForm,songForm,ratingForm,reviewForm
from .serializers import AlbumSerializers,RatingSerializers,ReviewSerializers,ProfileSerializers


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    get_music = Song.objects.all()
    context = {
        'musics':get_music
    }
    return render( request, 'index.html',context)







@login_required(login_url='login')
def profile(request):
    user= request.user
    context={ 'user': user}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def profiles(request,userID=None):
    if userID== None:
        userID=request.user.id
    # current_user= User.objects.get(id=userID)
    current_user= request.user
    user = current_user
    own_uploads= Song.objects.filter(username=current_user)
    profile = Profile.objects.all()
    context ={'songs':own_uploads, 'profile':profile,'user': current_user}
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def edit_profile(request):
    user= request.user
    if  request.method =='POST':
        form = EditProfileForm( request.POST, instance=user)
       
        if form.is_valid():
            form.save()
            
            return redirect ('profile')
    else:
        form =EditProfileForm(instance=request.user)
  
    context = {
        'form': form,
        
        'user': user
    }
    return render(request, 'profile_edit.html', context)
# if user remembers the password
def change_password(request):
    user = request.user
    if  request.method =='POST':
        form = PasswordChangeForm( data=request.POST, user=user)       
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # this will prevent user from being logged out after changing the pass
            return redirect('profile')
        else: # redirect the user if the form is not valid
            return redirect('change-password')
    else:
        form = PasswordChangeForm(user=user)
        context ={'form': form}
        return render(request, 'change_pass.html', context)
        







def song_post(request):
    current_user = request.user
    profile =Profile.objects.filter(user=current_user.id)    
    if request.method=="POST":
        post_form =songForm(request.POST,request.FILES, instance=current_user )
        if post_form.is_valid():           
            
            post = post_form.save()
        return redirect('/')
    else:
        post_form = songForm()
    title = " New Song"
    return render(request,'post_song.html',{"form":post_form, 'title': title})


def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/')



'''
############################################
***********    API *************************
############################################
'''
@api_view(['GET'])
def get_album(request):
    albums= Album.objects.all()
    if albums:
        serialize=AlbumSerializers(albums, many=True)
        return Response(serialize.data)
    else:
        return Response([])
    
@api_view(['GET'])
def get_ratings(request):
    ratings= Ratings.objects.all()
    if ratings:
        serialize=RatingSerializers(ratings, many=True)
        return Response(serialize.data)
    else:
        return Response([])
#Add rate to db    
@api_view(['POST'])
def add_rate(request):
    rating = request.data
    new_rating = Ratings(beats=rating['beats'],content=rating['content'],user=rating['user'])
    new_rating.save()
    return Response('Rating added successfully')


@api_view(['GET'])
def get_reviews(request):
    reviews= Review.objects.all()
    if reviews:
        serialize=ReviewSerializers(reviews, many=True)
        return Response(serialize.data)
    else:
        return Response([])
    

@api_view(['GET'])
def get_profiles(request):
    profiles= Profile.objects.all()
    if profiles:
        serialize=ProfileSerializers(profiles, many=True)
        return Response(serialize.data)
    else:
        return Response([])