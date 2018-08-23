from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from markdownx.models import MarkdownxField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField()
    text = MarkdownxField()
    cover = models.ImageField(upload_to='blog/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_edited']

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

def create_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(create_slug, sender=Post)
