from django_filters import rest_framework as filters

from core.models import RaceResultModel


class RaceResultFilter(filters.FilterSet):
    """DriverStanding Filter"""

    class Meta:
        model = RaceResultModel
        fields = '__all__'
