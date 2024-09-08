from django.urls import path

from app.views import IndexView, DriverStandingView, ConstructorStandingView, RaceResultView

app_name = "app"
urlpatterns = [
    path('', IndexView.as_view(), name='top'),
    path('driver_standing', DriverStandingView.as_view(), name='driver_standing'),
    path('constructor_standing', ConstructorStandingView.as_view(), name='constructor_standing'),
    path('race_result', RaceResultView.as_view(), name='race_result'),
]
