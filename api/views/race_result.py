from rest_framework import viewsets

from core.filters import RaceResultFilter
from core.models import RaceResultModel
from core.serializers import RaceResultSerializer


class RaceResultView(viewsets.ModelViewSet):
    """Race Result API"""

    queryset = RaceResultModel.objects.all()
    serializer_class = RaceResultSerializer
    filterset_class = RaceResultFilter
    ordering_fields = '__all__'
