from rest_framework import serializers

from core.models import DriverStandingModel, RaceResultModel, ConstructorStandingModel


class DriverStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverStandingModel
        fields = '__all__'


class RaceResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceResultModel
        fields = '__all__'


class ConstructorStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructorStandingModel
        fields = '__all__'
