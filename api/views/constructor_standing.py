from rest_framework import viewsets

from core.filters import ConstructorStandingFilter
from core.models import ConstructorStandingModel
from core.serializers import ConstructorStandingSerializer


class ConstructorStandingView(viewsets.ModelViewSet):
    """Constructor Standing API"""

    queryset = ConstructorStandingModel.objects.all()
    serializer_class = ConstructorStandingSerializer
    filterset_class = ConstructorStandingFilter
    ordering_fields = '__all__'
