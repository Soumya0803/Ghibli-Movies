from rest_framework import serializers
# from .models import Movie, Actors
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
# class ActorsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actors
#         fields = ['id', 'name', 'species', 'url']

# class MovieSerializer(serializers.ModelSerializer):
#     actors = ActorsSerializer(many=True, read_only=True)

#     class Meta:
#         model = Movie
#         fields = ['id', 'title', 'description', 'director', 'producer', 'release_date', 'running_time', 'rt_score', 'actors']
