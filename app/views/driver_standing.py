from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import DriverStandingModel


class DriverStandingView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # 現在の年度を取得
        year = datetime.now().year
        driver_standing = \
            DriverStandingModel.objects.filter(season=year).order_by('position').all()
        context = {
            'rankings': driver_standing
        }
        return render(request, 'app/driver_standing.html', context=context)
