from django.db import models
from django.db.models.deletion       import CASCADE
from django.db.models.fields.related import ManyToManyField

class Actor(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    class Meta:
        db_table = "actors"

class Movie(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actors       = models.ManyToManyField(Actor, through='ActorMovie', related_name='movies')

    class Meta:
        db_table = "movies"

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete= models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)

    class Meta:
        db_table = "actors_movies"