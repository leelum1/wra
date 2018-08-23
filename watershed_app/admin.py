from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Watershed, Picture
# Register your models here.

class WatershedAdmin(MarkdownxModelAdmin):
    list_display = ["name", "hydrometric_area"]
    prepopulated_fields = {"slug": ("name",)}

class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'watershed', 'photographer', 'capture_date',]

admin.site.register(Watershed, WatershedAdmin)
admin.site.register(Picture, PictureAdmin)
