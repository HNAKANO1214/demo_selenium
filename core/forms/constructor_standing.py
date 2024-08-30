from django import forms

from core.models import ConstructorStandingModel


class ConstructorStandingForm(forms.ModelForm):
    class Meta:
        model = ConstructorStandingModel
        fields = '__all__'
