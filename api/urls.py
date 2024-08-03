from django.urls import path, include
from rest_framework import routers

from .views import ConstructorStandingView, DriverStandingView, RaceResultView

router = routers.DefaultRouter()
router.register(r'race_result', RaceResultView)
router.register(r'driver_standing', DriverStandingView)
router.register(r'constructor_standing', ConstructorStandingView)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
]
