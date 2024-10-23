# from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from genres.models import Genre
from movies.forms import MovieModelForm
from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'genres' # objeto que irá para template

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
