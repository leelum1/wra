from django.contrib import admin
from .models import Abstraction_Point
# Register your models here.

class AbstractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'source_type', 'abstraction_rate',]

admin.site.register(Abstraction_Point, AbstractionAdmin)
