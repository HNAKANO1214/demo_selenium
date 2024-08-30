from django.db import models


class DriverStandingModel(models.Model):
    driver = models.CharField(max_length=50)
    position = models.IntegerField()
    nationality = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    season = models.IntegerField()

    def __str__(self) -> str:
        return self.driver

    class Meta:
        db_table = 'driver_standings'