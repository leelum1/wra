from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Book, BookRequest, SOP

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'author')
    search_fields = ('title', 'year')

class SOPAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'category',)
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(BookRequest)
admin.site.register(SOP, SOPAdmin)
