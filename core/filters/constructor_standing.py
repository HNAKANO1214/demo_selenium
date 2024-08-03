from django_filters import rest_framework as filters

from core.models import ConstructorStandingModel


class ConstructorStandingFilter(filters.FilterSet):
    """Constructor Standing Filter"""

    class Meta:
        model = ConstructorStandingModel
        fields = '__all__'
