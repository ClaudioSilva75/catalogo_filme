from django import forms

from movies.models import Movie


class MovieModelForm(forms.ModelForm):
    class Meta: # Reescrita da classe Meta
        model = Movie
        fields = '__all__' # uso de todos os campos disponíveis