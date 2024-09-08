from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import ConstructorStandingModel


class ConstructorStandingView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # 現在の年度を取得
        year = datetime.now().year
        constructor_standing = \
            ConstructorStandingModel.objects.filter(season=year).order_by('position').all()
        context = {
            'rankings': constructor_standing
        }
        return render(request, 'app/constructor_standing.html', context=context)
