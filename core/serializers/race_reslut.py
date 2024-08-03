from rest_framework import serializers

from core.models import RaceResultModel


class RaceResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceResultModel
        fields = '__all__'
