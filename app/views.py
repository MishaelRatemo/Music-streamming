from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import  logout as auth_logout
from django.contrib import messages

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
def profile(request,userID=None):
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
def create_edit_profile(request, username):
    # user = User.objects.get(username=username)
    current_user = request.user  
    create_profile= Profile.objects.filter(user_id=request.user.id)
    if create_profile.exists():        
        if request.method == 'POST':
            profile_form = profileForm(request.POST, request.FILES)
            if  profile_form.is_valid():
                profile_form.save()
                return redirect('/profile/', current_user)
        else:        
            profile_form = profileForm(instance=request.user.profile)       
    else:
        if request.method == 'POST':
            profile_form = profileForm(request.POST, request.FILES)
            if  profile_form.is_valid():
                profile_form.save()
                return redirect('/profile/', current_user)
        else:        
            profile_form = profileForm() 
           
    context = {
        'prof_form': profile_form, 
        'current_user': current_user
    }
    return render(request, 'profile_edit.html', context)

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