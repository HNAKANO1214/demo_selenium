from django.contrib import admin

from myapp.models import Drivers, Races, Teams


admin.site.register(Drivers)
admin.site.register(Races)
admin.site.register(Teams)
