from django.db import models
from django.urls import reverse
from datetime import datetime
from watershed_app.models import Watershed
from random import random

# Create your models here.
class Well(models.Model):
    name = models.CharField(max_length=80)
    index_no = models.CharField(max_length=10, primary_key=True)
    wellfield = models.CharField(max_length=80, blank=True, null=True)
    watershed = models.ForeignKey(Watershed, blank=True, null=True)
    depth = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    northing = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    easting = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    date_comm = models.DateField(null=True, blank=True)
    date_decomm = models.DateField(null=True, blank=True)
    needs_attn = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('groundwater_app:well_detail', kwargs={'pk':self.index_no})

    def __str__(self):
        return self.name

class GenericWell(models.Model):
    date = models.DateTimeField()
    reading = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True
        ordering = ['date']

    def fake(self):
        return self.reading * random() * 2

    def __str__(self):
        return self.date.strftime('%m/%d/%Y')

class EdwardTrace(GenericWell):
    pass

class Moka3(GenericWell):
    pass
