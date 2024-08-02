from django.db import models


class Races(models.Model):
    grand_prix = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)
    time = models.CharField(max_length=15)
