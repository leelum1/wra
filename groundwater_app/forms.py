from django.forms import ModelForm, SelectDateWidget
from .models import GenericWell

class WellForm(ModelForm):

    class Meta:
        model = GenericWell
        fields = ['date', 'reading']
        labels = {
            'date': 'Date of metering',
            'reading': 'Reading in meters',
        }
        initial = {
            'date': '01-01-2010',
        }
        help_texts = {
            'readings': 'reduced levels are autocmatically calculated from the benchmark',
        }
        widgets = {
            'date': SelectDateWidget,
        }
