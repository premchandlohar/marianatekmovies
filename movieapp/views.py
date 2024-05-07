from django.http import JsonResponse
from django.core import serializers
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()

    genre = request.GET.get('genre')
    if genre:
        movies = movies.filter(genre__icontains=genre)

    search_query = request.GET.get('search')
    if search_query:
        movies = movies.filter(title__icontains=search_query)

    serialized_movies = [
        {
            'title': movie.title,
            'poster': movie.poster,
            'genre': movie.genre,
            'rating': movie.rating,
            'year_release': movie.year_release,
            'metacritic_rating': movie.metacritic_rating,
            'runtime': movie.runtime,
        }
        for movie in movies
    ]

    return JsonResponse({'movies': serialized_movies}, safe=False)