from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import DriverStandingModel


class DriverStandingView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # 現在の年度を取得
        default_year = request.GET.get('year', datetime.now().year)
        driver_standing = \
            DriverStandingModel.objects.filter(season=default_year).order_by('position').all()
        years = []
        for year in DriverStandingModel.objects.values('season').order_by('-season').distinct():
            years.append(str(year['season']))
        context = {
            'rankings': driver_standing,
            'default_year': default_year,
            'years': years,
        }
        return render(request, 'app/driver_standing.html', context=context)
