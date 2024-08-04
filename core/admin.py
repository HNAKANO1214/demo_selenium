from django.contrib import admin

from core.forms import (
    ConstructorStandingForm, DriverStandingForm, RaceResultForm
)
from core.models import (
    ConstructorStandingModel, DriverStandingModel, RaceResultModel
)


class ConstructorStandingAdmin(admin.ModelAdmin):
    form = ConstructorStandingForm
    exclude = []


class DriverStandingForm(admin.ModelAdmin):
    form = DriverStandingForm
    exclude = []


class RaceResultForm(admin.ModelAdmin):
    form = RaceResultForm
    exclude = []


admin.site.register(ConstructorStandingModel, ConstructorStandingAdmin)
admin.site.register(DriverStandingModel, DriverStandingForm)
admin.site.register(RaceResultModel, RaceResultForm)
