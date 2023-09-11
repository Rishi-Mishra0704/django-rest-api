from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Actor, Movie
from .serializer import ActorSerializer, MovieSerializer

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def actor_create(request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)