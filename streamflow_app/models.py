from django.db import models
from django.urls import reverse
from asset_app.models import User
from data_app.choices import WATERSHEDS
from random import random


# Create your models here.
class FuessGauge(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    river = models.CharField(max_length=80)
    watershed = models.CharField(max_length=50, choices=WATERSHEDS)
    northing = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    easting = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    date_comm = models.DateField(null=True, blank=True)
    date_decomm = models. DateField(null=True, blank=True)
    needs_attn = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)

class MeteringSite(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, primary_key=True)
    watershed = models.CharField(max_length=50)
    category = models.CharField(max_length = 50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/meterings', blank=True)
    northing = models.DecimalField(max_digits=12, decimal_places=8, blank=True)
    easting = models.DecimalField(max_digits=12, decimal_places=8, blank=True)

    class Meta:
        ordering = ['code']

    def get_absolute_url(self):
        return reverse('data_app:metering_detail', kwargs={'pk':self.code})

    def __str__(self):
        return self.name


class GenericMetering(models.Model):
    date = models.DateField(primary_key=True)
    discharge = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('streamflow_app:metering_list')

    def toMGD(self):
        return self.discharge * 220 * 86400 / 1000000 * random() * 2

    def fake(self):
        return self.discharge * random() * 2

class Acono(GenericMetering):
    pass

class Aripo(GenericMetering):
    pass

class Arouca(GenericMetering):
    pass

class Capriata(GenericMetering):
    pass

class Caura(GenericMetering):
    pass

class Damier(GenericMetering):
    pass

class Guanapo(GenericMetering):
    pass

class LasCuevas(GenericMetering):
    pass

class Lluengo(GenericMetering):
    pass

class Lopinot(GenericMetering):
    pass

class Maraval(GenericMetering):
    pass

class Marianne(GenericMetering):
    pass

class Matura(GenericMetering):
    pass

class Naranjo(GenericMetering):
    pass

class NorthOropouche(GenericMetering):
    pass

class Quare(GenericMetering):
    pass

class Rincon(GenericMetering):
    pass

class Tompire(GenericMetering):
    pass

class Yarra(GenericMetering):
    pass
