from django.db import models


class RaceResultModel(models.Model):
    grand_prix = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)
    time = models.CharField(max_length=15)
    season = models.IntegerField()

    def __str__(self) -> str:
        return self.grand_prix
