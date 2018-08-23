from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post
# Register your models here.
class PostAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'date_created']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
