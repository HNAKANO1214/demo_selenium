from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import RaceResultModel


class RaceResultView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # 現在の年度を取得
        year = datetime.now().year
        race_results = RaceResultModel.objects.filter(season=year).order_by('-race_date').all()
        context = {
            'rankings': race_results
        }
        return render(request, 'app/race_result.html', context=context)
