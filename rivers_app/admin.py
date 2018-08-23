from django.contrib import admin
from .models import River

class RiverAdmin(admin.ModelAdmin):
    list_display = ['name', 'watershed', 'length',]

# Register your models here.
admin.site.register(River, RiverAdmin)
