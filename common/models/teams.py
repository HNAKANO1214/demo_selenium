from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=50)
    position = models.IntegerField()
    points = models.IntegerField()
