from django.views.generic import TemplateView
from django.apps import apps
from data_app.models import RainGauge
from .models import Index
# Create your views here.

class SPITemplateView(TemplateView):
    template_name = 'spi_app/spi.html'

    def get_context_data(self, **kwargs):
        ctx = super(SPITemplateView, self).get_context_data(**kwargs)
        ctx['gauges'] = ['Columbia Estate', 'Hollis', 'La Regalada', 'River Estate', 'San Antonio Estate', 'UWI Field Station']

        if self.request.GET.get('gauge'):
            name = self.request.GET.get('gauge').replace('_', ' ')
            gauge = RainGauge.objects.get(name=name)
            ctx['selected_gauge'] = gauge
            if self.request.GET.get('start') and self.request.GET.get('end'):
                start = self.request.GET.get('start')
                end = self.request.GET.get('end')
                ctx['data'] = Index.objects.filter(gauge=gauge).filter(year__range=[start, end]).order_by('year', 'month')
            else:
                ctx['data'] = Index.objects.filter(gauge=gauge).order_by('year', 'month')
        return ctx

    def get(self, request, *args, **kwargs):
        # if self.request.GET.get('gauge'):
        #     print('hello')
        #     name = self.request.GET.get('gauge').replace('_', ' ')
        #     gauge = RainGauge.objects.get(name=name)
        #     if self.request.GET.get('start') and self.request.GET.get('end'):
        #         start = self.request.GET.get('start')
        #         end = self.request.GET.get('end')
        return super(SPITemplateView, self).get(request, *args, **kwargs)
