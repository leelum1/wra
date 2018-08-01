from django.forms import ModelForm, SelectDateWidget
from .models import GenericMetering

class MeteringForm(ModelForm):

    class Meta:
        model = GenericMetering
        fields = ['date', 'discharge']
        labels = {
            'date': 'Date of metering',
            'discharge': 'Discharge in cumecs',
        }
        initial = {
            'date': '01-01-2010',
        }
        help_texts = {
            'discharge': 'cumecs are automatically converted to MGD',
        }
        widgets = {
            'date': SelectDateWidget,
        }
