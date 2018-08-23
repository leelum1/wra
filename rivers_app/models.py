from django.db import models
from watershed_app.models import Watershed

# Create your models here.
class River(models.Model):
    name = models.CharField(max_length=125)
    watershed = models.ForeignKey(Watershed, on_delete=models.CASCADE)
    length = models.FloatField(null=True, blank=True)

    def length_to_km(self):
        return (self.length / 1000)

    def __str__(self):
        return self.name
