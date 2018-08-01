from django.db import models
from django.core.urlresolvers import reverse
from asset_app.models import User
from watershed_app.models import Watershed
from .choices import CATEGORY, WATERSHEDS
from random import random


# Create your models here.
class RainGauge(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    code = models.CharField(max_length=10, primary_key=True)
    category = models.CharField(max_length=45, choices=CATEGORY)
    serial_no = models.CharField(max_length=45, null=True, blank=True)
    watershed = models.CharField(max_length=50, choices=WATERSHEDS)
    northing = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    easting = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    date_comm = models.DateField(null=True, blank=True)
    date_decomm = models. DateField(null=True, blank=True)
    needs_attn = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('data_app:gaugedetail', kwargs={'pk':self.code})

    def __str__(self):
        return self.name

class GaugeReader(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=80)
    phone = models.PositiveIntegerField()
    gauge = models.ForeignKey(RainGauge, null=True, blank=True)
    house_no = models.CharField(max_length=20)
    street_name = models.CharField(max_length=80)
    town = models.CharField(max_length=80)

    def __str__(self):
        return self.first_name + " " + self.last_name

class GenericPotGaugeRecord(models.Model):
    date = models.DateField(primary_key=True)
    rainfall = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['date']

    def toinches(self):
        return self.rainfall * 0.0393701 * random() * 2

    def fake(self):
        return self.rainfall * random() * 2

class ArenaPlantation(GenericPotGaugeRecord):
    pass

class AsaWright(GenericPotGaugeRecord):
    pass

class BlanchisseusePolice(GenericPotGaugeRecord):
    pass

class BotanicGardens(GenericPotGaugeRecord):
    pass

class BrassoParia(GenericPotGaugeRecord):
    pass

class ChathamGovernment(GenericPotGaugeRecord):
    pass

class ColumbiaEstate(GenericPotGaugeRecord):
    pass

class ConstanceEstate(GenericPotGaugeRecord):
    pass

class CumanaVillage(GenericPotGaugeRecord):
    pass

class CumutoPine(GenericPotGaugeRecord):
    pass

class ElSusanEstate(GenericPotGaugeRecord):
    pass

class FishingPond(GenericPotGaugeRecord):
    pass

class FreeportWaterworks(GenericPotGaugeRecord):
    pass

class GordonMiller(GenericPotGaugeRecord):
    pass

class GranvilleWaterworks(GenericPotGaugeRecord):
    pass

class GrosnevorEstate(GenericPotGaugeRecord):
    pass

class Hollis(GenericPotGaugeRecord):
    pass

class LaRegalada(GenericPotGaugeRecord):
    pass

class MarperFarm(GenericPotGaugeRecord):
    pass

class MatelotRestHouse(GenericPotGaugeRecord):
    pass

class MaturaPolice(GenericPotGaugeRecord):
    pass

class MelajoPlantation(GenericPotGaugeRecord):
    pass

class Navet(GenericPotGaugeRecord):
    pass

class NavetPresbyterian(GenericPotGaugeRecord):
    pass

class Newlands(GenericPotGaugeRecord):
    pass

class OrtoireEstate(GenericPotGaugeRecord):
    pass

class PenalWaterworks(GenericPotGaugeRecord):
    pass

class PerseveranceEstate(GenericPotGaugeRecord):
    pass

class Petrotrin(GenericPotGaugeRecord):
    pass

class Piarco(GenericPotGaugeRecord):
    pass

class PointFortinWTP(GenericPotGaugeRecord):
    pass

class Pure(GenericPotGaugeRecord):
    pass

class RiverEstate(GenericPotGaugeRecord):
    pass

class SanAntonio(GenericPotGaugeRecord):
    pass

class SanAntonioEstate(GenericPotGaugeRecord):
    pass

class SanJuan(GenericPotGaugeRecord):
    pass

class SanPedroEstate(GenericPotGaugeRecord):
    pass

class SanQuintinEstate(GenericPotGaugeRecord):
    pass

class SansSouci(GenericPotGaugeRecord):
    pass

class SantaMariaEstate(GenericPotGaugeRecord):
    pass

class SinghsEstate(GenericPotGaugeRecord):
    pass

class TCLClaxtonBay(GenericPotGaugeRecord):
    pass

class TCLMayo(GenericPotGaugeRecord):
    pass

class Torrecilla(GenericPotGaugeRecord):
    pass

class TortugaEstate(GenericPotGaugeRecord):
    pass

class TrinidadLakeAsphalt(GenericPotGaugeRecord):
    pass

class UWI(GenericPotGaugeRecord):
    pass

class UWIFieldStation(GenericPotGaugeRecord):
    pass

class ValenciaRange(GenericPotGaugeRecord):
    pass
