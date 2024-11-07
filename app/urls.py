"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, LogoutView, RegisterView
from movies.views import (MovieDeleteView, MoviesDetailView, MoviesListView,
                          MovieUpdateView, NewMovieCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # path('', MoviesListView.as_view(), name='movies_list'),
    path('movies/', MoviesListView.as_view(), name='movies_list'),
    path('movies/<int:pk>/', MoviesDetailView.as_view(), name='movie_detail'),
    path('movie/<int:pk>update/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('new_movie/', NewMovieCreateView.as_view(), name='new_movie'),

]

# Habilita uso de mídias no projeto
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
