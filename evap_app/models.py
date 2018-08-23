from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=128)
    code = models.FloatField(primary_key=True)
    

    def __str__(self):
        return self.name
