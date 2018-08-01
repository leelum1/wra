from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from datetime import datetime
from statistics import mean, stdev
import json
from .forms import MeteringForm
from . import recession
from .models import FuessGauge, MeteringSite

class FuessListView(ListView):
    model = FuessGauge
    template_name = "streamflow_app/fuess_list.html"
    context_object_name = "gauges"

class MeteringListView(ListView):
    model = MeteringSite
    template_name = 'streamflow_app/metering_list.html'
    context_object_name = 'meterings'

class MeteringDetailView(DetailView):
    model = MeteringSite
    context_object_name = 'metering'
    template_name = 'streamflow_app/metering_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(MeteringDetailView, self).get_context_data(**kwargs)
        current_gauge = MeteringSite.objects.get(code=self.kwargs['pk'])
        gauge_name = current_gauge.name.replace(' ', '')
        model = apps.get_model('streamflow_app', gauge_name)
        ctx['north'] = current_gauge.northing
        ctx['east'] = current_gauge.easting

        record_start = model.objects.order_by('date').first().date
        record_end = model.objects.order_by('date').last().date
        ctx['defaultstart'] = record_start
        ctx['defaultend'] = record_end

        if self.request.GET.get('startdate') and self.request.GET.get('enddate'):
            startdate = self.request.GET.get('startdate')
            enddate = self.request.GET.get('enddate')
            ctx['startdate'] = datetime.strptime(startdate, '%Y-%m-%d')
            ctx['enddate'] = datetime.strptime(enddate, '%Y-%m-%d')

            ctx['meterings'] = model.objects.filter(date__range=[startdate, enddate])

        else:
            ctx['meterings'] = model.objects.all()

        return ctx

class MeteringCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    template_name = 'streamflow_app/create_metering.html'
    form_class = MeteringForm

    #Get model
    def get(self, request, *args, **kwargs):
        current_gauge = MeteringSite.objects.get(code=self.kwargs['pk'])
        gauge_name = current_gauge.name.replace(' ', '')
        self.model = apps.get_model('streamflow_app', gauge_name)
        return super(MeteringCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(MeteringCreateView, self).get_context_data(**kwargs)
        ctx['name'] = self.model.__name__
        ctx['code'] = self.kwargs['pk']
        return ctx

    def post(self, request, *args, **kwargs):
        current_gauge = MeteringSite.objects.get(code=self.kwargs['pk'])
        gauge_name = current_gauge.name.replace(' ', '')
        self.model = apps.get_model('streamflow_app', gauge_name)
        return super(MeteringCreateView, self).post(request, *args, **kwargs)

class RecessionTemplateView(TemplateView):
    template_name = 'streamflow_app/recession.html'

    def get_context_data(self, **kwargs):
        ctx = super(RecessionTemplateView, self).get_context_data(**kwargs)
        current_gauge = MeteringSite.objects.get(code=self.kwargs['pk'])
        gauge_name = current_gauge.name.replace(' ', '')
        get_model = apps.get_model('streamflow_app', gauge_name)
        ctx['name'] = get_model.__name__
        ctx['code'] = self.kwargs['pk']

        #create dictionary of year and rainfall
        raw_streamflow = {}
        for metering in get_model.objects.all():
            if metering.date.month < 6:
                current_metering = get_model.objects.get(date=metering.date)
                raw_streamflow[current_metering.date] = current_metering.discharge

        #call recession functions
        flows = recession.flow_freq(recession.recession(raw_streamflow))
        ctx['flows'] = flows
        ctx['records'] = json.dumps(flows)

        return ctx
