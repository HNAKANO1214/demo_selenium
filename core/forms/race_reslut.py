from django import forms

from core.models import RaceResultModel


class RaceResultForm(forms.ModelForm):
    class Meta:
        models = RaceResultModel
        fields = '__all__'
