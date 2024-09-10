from datetime import datetime
from django.views.generic import View
from django.shortcuts import render

from core.models import ConstructorStandingModel


class ConstructorStandingView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        default_year = request.GET.get('year', datetime.now().year)
        constructor_standing = \
            ConstructorStandingModel.objects.filter(season=default_year).order_by('position').all()
        years = []
        for year in ConstructorStandingModel.objects.values('season').order_by('-season').distinct():
            years.append(str(year['season']))
        context = {
            'rankings': constructor_standing,
            'default_year': default_year,
            'years': years,
        }
        return render(request, 'app/constructor_standing.html', context=context)
