from django.db import models


class RaceResultModel(models.Model):
    grand_prix = models.CharField(max_length=50)
    race_date = models.DateField(default=None)
    winner = models.CharField(max_length=50)
    car = models.CharField(max_length=50, default='')
    laps = models.IntegerField(default=0)
    race_time = models.CharField(max_length=15)
    season = models.IntegerField()

    def __str__(self) -> str:
        return self.grand_prix

    class Meta:
        unique_together = (('grand_prix', 'season'),)
