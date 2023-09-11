from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.ManyToManyField('Actor', related_name='movies')

    def __str__(self):
        return self.title