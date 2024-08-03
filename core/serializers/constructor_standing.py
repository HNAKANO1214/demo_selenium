from rest_framework import serializers

from core.models import ConstructorStandingModel


class ConstructorStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructorStandingModel
        fields = '__all__'
