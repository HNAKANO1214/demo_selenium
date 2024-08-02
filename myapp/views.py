from rest_framework import viewsets


class RaceResult(viewsets.ModelViewSet):
    """プロフィールページのビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        print("get関数が呼ばれました")
