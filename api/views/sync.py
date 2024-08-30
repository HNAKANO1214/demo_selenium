from rest_framework.views import APIView
from rest_framework.response import Response

from core.tasks.sync import sync_constructor_standings, sync_driver_standingss, sync_race_results


class SyncConstructorStandingViews(APIView):
    """Sync Constructor Standings API"""

    def post(self, request):
        return Response({"status": "success"})


class SyncDriverStandingsView(APIView):
    """Sync Driver Standingss API"""

    def post(self, request):
        return Response({"status": "success"})


class SyncRaceResultsView(APIView):
    """Sync RaceResults View API"""

    def post(self, request):
        sync_race_results.sync()
        return Response({"status": "success"})
