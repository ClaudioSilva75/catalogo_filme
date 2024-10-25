from django import forms

from movies.models import Movie


class MovieModelForm(forms.ModelForm):
    # Reescrita da classe Meta
    class Meta:
        model = Movie
        # uso de todos os campos disponíveis
        fields = '__all__'
