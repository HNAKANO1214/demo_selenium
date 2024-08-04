from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from .views import ConstructorStandingView, DriverStandingView, RaceResultView, SyncView

router = routers.DefaultRouter()
router.register(r'race_result', RaceResultView)
router.register(r'driver_standing', DriverStandingView)
router.register(r'constructor_standing', ConstructorStandingView)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += [path("sync/", SyncView.as_view())]
