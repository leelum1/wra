from django.contrib import admin
from .models import GaugeReader, RainGauge

class ReaderAdmin(admin.ModelAdmin):
    list_display = ['phone', 'gauge']

class RainAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'watershed']

admin.site.register(GaugeReader, ReaderAdmin)
admin.site.register(RainGauge, RainAdmin)
