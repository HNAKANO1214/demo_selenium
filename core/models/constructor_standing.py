from django.db import models


class ConstructorStandingModel(models.Model):
    constructor = models.CharField(max_length=50)
    position = models.IntegerField()
    points = models.IntegerField()
    season = models.IntegerField()

    def __str__(self) -> str:
        return self.constructor