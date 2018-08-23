from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField

# Create your models here.
class Watershed(models.Model):
    AREAS = (
        (1, 'North Coast'),
        (2, 'North Oropouche'),
        (3, 'Nariva'),
        (4, 'Ortoire'),
        (5, 'Southern Range'),
        (6, 'Cedros Peninsula'),
        (7, 'South Oropouche'),
        (8, 'Central West Coast'),
        (9, 'Western Peninsula'),
        (11, 'Leeward'),
        (12, 'East Coast'),
        (13, 'Windward'),
        (14, 'Courland'),
        (15, 'Lowlands'),
    )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    hydrometric_area = models.PositiveSmallIntegerField(choices=AREAS)
    area = models.FloatField()
    description = MarkdownxField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('watershed_app:detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=512)
    watershed = models.ForeignKey(Watershed, on_delete=models.CASCADE)
    photographer = models.CharField(max_length=225, null=True, blank=True)
    capture_date = models.DateTimeField(null=True, blank=True)
    uploaddate = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='watersheds/pictures/', max_length=225, help_text='Vertical height of 500px or size of 100 kB.')
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('watershed_app:detail', args=[str(self.watershed.slug)])

    def __str__(self):
        return self.title
