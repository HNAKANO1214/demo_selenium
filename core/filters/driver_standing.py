from django_filters import rest_framework as filters

from core.models import DriverStandingModel


class DriverStandingFilter(filters.FilterSet):
    """DriverStanding Filter"""

    class Meta:
        model = DriverStandingModel
        fields = '__all__'
