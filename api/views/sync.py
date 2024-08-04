from rest_framework.views import APIView
from rest_framework.response import Response

from core.tasks.sync import sync


class SyncView(APIView):
    """Sync API"""

    def post(self, request):
        sync()
        return Response({"status": "success"})
