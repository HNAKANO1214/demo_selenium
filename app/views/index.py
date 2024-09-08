from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import ConstructorStandingModel, DriverStandingModel, RaceResultModel


class IndexView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # 現在の年度を取得
        year = datetime.now().year
        # 最初の5件のみ
        race_results = RaceResultModel.objects.filter(season=year).order_by('-race_date').all()[:5]
        driver_standings = \
            DriverStandingModel.objects.filter(season=year).order_by('position').all()
        constructor_standings = \
            ConstructorStandingModel.objects.filter(season=year).order_by('position').all()
        context = {
            'race_results': race_results,
            'driver_standings': driver_standings,
            'constructor_standings': constructor_standings
        }
        return render(request, 'app/index.html', context=context)
