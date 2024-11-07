# from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from genres.models import Genre
from movies.forms import MovieModelForm
from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    # objeto que irá para template
    context_object_name = 'genres'

    def get_queryset(self):
        queryset = Genre.objects.prefetch_related('movies').all()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(movies__title__icontains=search).distinct()

        return queryset


class MoviesDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


class NewMovieCreateView(CreateView):
    model = Movie
    form_class = MovieModelForm
    template_name = 'movies/new_movie.html'
    success_url = '/movies/'


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieModelForm
    template_name = 'movies/movie_update.html'
    success_url = '/movies/'


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = '/movies/'
