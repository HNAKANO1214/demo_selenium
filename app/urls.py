from django.urls import path

from app.views import IndexView

app_name = "app"
urlpatterns = [
    path('', IndexView.as_view(), name='top'),
]
