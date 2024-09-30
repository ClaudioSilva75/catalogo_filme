# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
    template_name = 'base.html'
    context_object_name = 'movies' # objeto que irá para template

class MoviesDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    