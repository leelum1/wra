from django.views.generic import TemplateView
from django.shortcuts import render
from data_app.models import RainGauge
from groundwater_app.models import Well
from streamflow_app.models import MeteringSite

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class DataView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        ctx = super(DataView, self).get_context_data(**kwargs)
        ctx['rain'] = RainGauge.objects.all().count
        ctx['wells'] = Well.objects.all().count
        ctx['rivers'] = MeteringSite.objects.all().count
        return ctx

class LegalTemplateView(TemplateView):
    template_name = 'legal.html'

class BirthdayTemplateView(TemplateView):
    template_name = 'birthday.html'

def google_verify(request):
    return render(request, 'googlea70085b6066e71d7.html')
