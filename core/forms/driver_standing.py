from django import forms

from core.models import DriverStandingModel


class DriverStandingForm(forms.ModelForm):
    class Meta:
        models = DriverStandingModel
        fields = '__all__'
