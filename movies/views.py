import requests
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MovieList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Check if cached data is available
        movie_cache = cache.get('ghibli_movies')

        if movie_cache:
            return Response(movie_cache)

        response = requests.get("https://ghibli.rest/films")

        if response.status_code == 200:
            movies = response.json()

            for movie in movies:
                # filter based on 1 min time
                movie['actors'] = self.get_actors(movie.get('people', []))
                movie.pop('people', None)

            response_data = {
                'status': "ok",
                'movies': movies,
            }

            # Cache movies for 60 sec
            cache.set('ghibli_movies', response_data, 60)

            return Response(response_data)

        return Response({'status': "error", 'message': 'Unable to fetch ghibli movies'})

    def get_actors(self, all_people):
        actors = []

        for people_url in all_people:
            response = requests.get(people_url)
            if response.status_code == 200:
                data_list = response.json()
                for data in data_list:
                    actor_data = {
                        "id": data.get("id", ''),
                        "name": data.get("name", ''),
                        'species': data.get('species', ''),
                        'url': data.get('url', '')
                    }
                    actors.append(actor_data)
            
        return actors
        