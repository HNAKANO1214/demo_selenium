from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from .views import (
    ConstructorStandingView, DriverStandingView, RaceResultView,
)

router = routers.DefaultRouter()
router.register(r'race_result', RaceResultView)
router.register(r'driver_standing', DriverStandingView)
router.register(r'constructor_standing', ConstructorStandingView)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    from .views import (
        SyncConstructorStandingViews, SyncDriverStandingsView, SyncRaceResultsView
    )
    urlpatterns += [
        path("sync_constructor_standings/", SyncConstructorStandingViews.as_view()),
        path("sync_driver_standings/", SyncDriverStandingsView.as_view()),
        path("sync_race_results/", SyncRaceResultsView.as_view()),
    ]
