from django import forms

from core.models import ConstructorStandingModel


class ConstructorStandingForm(forms.ModelForm):
    class Meta:
        models = ConstructorStandingModel
        fields = '__all__'
