from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Watershed
# Register your models here.

class WatershedAdmin(MarkdownxModelAdmin):
    list_display = ["name", "hydrometric_area"]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Watershed, WatershedAdmin)
