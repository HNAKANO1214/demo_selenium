from django.db import models


class DriverStandingModel(models.Model):
    driver = models.CharField(max_length=50)
    position = models.IntegerField()
    nationality = models.CharField(max_length=50)
    team = models.CharField(max_length=50, null=True, blank=True, default=None)
    points = models.FloatField()
    season = models.IntegerField()

    def __str__(self) -> str:
        return self.driver

    class Meta:
        db_table = 'driver_standings'
