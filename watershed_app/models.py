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
