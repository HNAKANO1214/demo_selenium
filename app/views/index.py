from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
    """初期表示用のビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        return render(request, 'app/index.html')
