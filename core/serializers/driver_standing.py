from rest_framework import serializers

from core.models import DriverStandingModel


class DriverStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverStandingModel
        fields = '__all__'
