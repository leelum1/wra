from django.contrib import admin
from .models import FuessGauge, MeteringSite

# Register your models here.
class MeteringAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'watershed', 'category']

class FuessAdmin(admin.ModelAdmin):
    list_display = ['code', 'river', 'watershed', 'needs_attn']

admin.site.register(MeteringSite, MeteringAdmin)
admin.site.register(FuessGauge, FuessAdmin)
