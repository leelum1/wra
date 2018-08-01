from django.db import models
from django.urls import reverse

# Create your models here.
class Caroni(models.Model):
    date = models.DateField(primary_key=True)
    rainfall = models.FloatField(blank=True, null=True)
    level = models.FloatField()
    production = models.FloatField(blank=True, null=True)
    release = models.FloatField(blank=True, null=True)
    pump = models.FloatField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('reservoir_app:caroni')

    def __str__(self):
        return self.date

class Navet(models.Model):
    date = models.DateField(primary_key=True)
    rainfall = models.FloatField(blank=True, null=True)
    level = models.FloatField()
    production = models.FloatField(blank=True, null=True)
    pump = models.FloatField(blank=True, null=True)

class Hollis(models.Model):
    date = models.DateField(primary_key=True)
    rainfall = models.FloatField(blank=True, null=True)
    level = models.FloatField()
    production = models.FloatField(blank=True, null=True)

class Hillsborough(models.Model):
    date = models.DateField(primary_key=True)
    rainfall = models.FloatField(blank=True, null=True)
    level = models.FloatField()
    production = models.FloatField(blank=True, null=True)
