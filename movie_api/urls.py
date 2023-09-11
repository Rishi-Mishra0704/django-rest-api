from django.urls import path

from . import views

urlpatterns = [
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/create/', views.actor_create, name='actor_create'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/create/', views.movie_create, name='movie_create'),
]