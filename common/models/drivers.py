from django.db import models


class Drivers(models.Model):
    name = models.CharField(max_length=50)
    position = models.IntegerField()
    nationality = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    points = models.IntegerField()
