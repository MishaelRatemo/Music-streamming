from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Album, Ratings, Review, Profile, Song, User
from .serializers import AlbumSerializers,RatingSerializers,ReviewSerializers,ProfileSerializers


# Create your views here.
def index(request):
    
    return render( request, 'index.html')

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