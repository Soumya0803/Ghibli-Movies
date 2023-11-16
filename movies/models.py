# from django.db import models

# # Create your models here.

# class Actors(models.Model):
#     actor_id = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     species = models.CharField(max_length=100)
#     url = models.URLField()

# class Movie(models.Model):
#     movie_id = models.CharField(max_length=100)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     director = models.CharField(max_length=100)
#     producer = models.CharField(max_length=100)
#     release_date = models.DateField()
#     running_time = models.IntegerField()
#     rt_score = models.CharField(max_length=20)
#     actors = models.ManyToManyField(Actors)

