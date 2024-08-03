from rest_framework import viewsets

from core.models import ConstructorStandingModel
from core.serializers import ConstructorStandingSerializer


class ConstructorStandingView(viewsets.ModelViewSet):
    """Constructor Standing API"""

    queryset = ConstructorStandingModel.objects.all()
    serializer_class = ConstructorStandingSerializer
