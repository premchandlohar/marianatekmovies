from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField()
    genre = models.CharField(max_length=50)
    rating = models.FloatField()
    year_release = models.IntegerField()
    metacritic_rating = models.FloatField()
    runtime = models.IntegerField()

    class Meta:
        ordering = ['-id']