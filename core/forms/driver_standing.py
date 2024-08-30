from django import forms

from core.models import DriverStandingModel


class DriverStandingForm(forms.ModelForm):
    class Meta:
        model = DriverStandingModel
        fields = '__all__'
