from django.db import models
from asset_app.models import User

class Abstraction_Point(models.Model):
    SOURCES = (
        ('Rainfall', 'Rainfall'),
        ('River', 'River'),
        ('Spring', 'Spring'),
        ('Well', 'Well'),
    )
    name = models.CharField(max_length=80)
    company = models.ForeignKey(User)
    source_type = models.CharField(max_length=80, choices=SOURCES)
    abstraction_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    abstraction_period = models.CharField(max_length=80, blank=True, null=True)
