from django import forms
from django.core.exceptions import ValidationError

from core.models import RaceResultModel


class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResultModel
        fields = '__all__'

    @staticmethod
    def check_unique(
        race_results: list, grand_prix: str, race_date: str, season: str
    ) -> bool:
        for race_result in race_results:
            if race_result.grand_prix == grand_prix\
                    and race_result.race_date == race_date and race_result.season == season:
                return False
        return True

    @staticmethod
    def check_exists_season(season: str, grand_prix: str) -> None:
        if RaceResultModel.objects.filter(season=season, grand_prix=grand_prix).exists():
            return True
        return False
