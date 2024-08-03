from rest_framework import routers

from .views import ConstructorStandingView, DriverStandingView, RaceResultView

router = routers.DefaultRouter()
router.register('race_reslut', RaceResultView)
router.register('driver_standing', DriverStandingView)
router.register('constructor_standing', ConstructorStandingView)
