from rest_framework import viewsets

from core.models import DriverStandingModel
from core.serializers import DriverStandingSerializer


class DriverStandingView(viewsets.ModelViewSet):
    """Driver Standing API"""

    queryset = DriverStandingModel.objects.all()
    serializer_class = DriverStandingSerializer
