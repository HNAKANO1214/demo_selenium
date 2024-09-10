from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import RaceResultModel


class RaceResultView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # 現在の年度を取得
        default_year = request.GET.get('year', datetime.now().year)
        race_results = RaceResultModel.objects.filter(season=default_year).order_by('-race_date').order_by('-season').all()
        years = []
        for year in RaceResultModel.objects.values('season').order_by('-season').distinct():
            years.append(str(year['season']))
        context = {
            'rankings': race_results,
            'default_year': default_year,
            'years': years,
        }
        return render(request, 'app/race_result.html', context=context)
