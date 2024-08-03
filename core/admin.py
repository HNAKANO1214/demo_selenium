from django.contrib import admin

from core.forms import (
    ConstructorStandingForm, DriverStandingForm, RaceResultForm
)
from core.models import (
    ConstructorStandingModel, DriverStandingModel, RaceResultModel
)


class ConstructorStandingAdmin(admin.ModelAdmin):
    form = ConstructorStandingForm
    list_display = ('constructor', 'season', 'position', 'points')


class DriverStandingForm(admin.ModelAdmin):
    form = DriverStandingForm
    list_display = ('driver', 'season', 'position', 'nationality', 'team', 'points')


class RaceResultForm(admin.ModelAdmin):
    form = RaceResultForm
    list_display = ('grand_prix', 'winner', 'time', 'season')


admin.site.register(ConstructorStandingModel, ConstructorStandingAdmin)
admin.site.register(DriverStandingModel, DriverStandingForm)
admin.site.register(RaceResultModel, RaceResultForm)
