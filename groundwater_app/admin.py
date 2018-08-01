from django.contrib import admin
from .models import Well

class WellAdmin(admin.ModelAdmin):
    list_display = ['name', 'index_no', 'wellfield']

# Register your models here.
admin.site.register(Well, WellAdmin)
