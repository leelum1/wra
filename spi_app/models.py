from django.db import models
from data_app.models import RainGauge

# Create your models here.
class Index(models.Model):
    gauge = models.ForeignKey(RainGauge, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    one_month = models.FloatField()
    three_month = models.FloatField()
    six_month = models.FloatField()
    twelve_month = models.FloatField()

    def remove_null(self):
        if self.one_month == -99:
            return '-'

        if self.three_month == -99:
            return '-'

        if self.six_month == -99:
            return '-'

        if self.twelve_month == -99:
            return '-'

    def to_months(self):
        months = {1: "January",
                    2: "February",
                    3: "March",
                    4: "April",
                    5: "May",
                    6: "June",
                    7: "July",
                    8: "August",
                    9: "September",
                    10: "October",
                    11: "November",
                    12: "December",}

        return months[self.month]
