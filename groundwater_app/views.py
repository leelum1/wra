from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from .forms import WellForm
from .models import Well
from datetime import datetime
import json

class WellListView(ListView):
    model = Well
    context_object_name = 'wells'
    template_name = 'groundwater_app/groundwater.html'

class WellDetailView(DetailView):
    model = Well
    context_object_name = 'well'
    template_name = 'groundwater_app/well_detail.html'

    # def get_context_data(self, **kwargs):
    #     ctx = super(WellDetailView, self).get_context_data(**kwargs)
    #     current_well = Well.objects.get(index_no=self.kwargs['pk'])
    #     well_name = current_well.name.replace(' ', '')
    #     model = apps.get_model('groundwater_app', well_name)
    #     self.request.session['wellname'] = well_name
    #     self.request.session['name'] = current_well.name
    #     self.request.session['index_no'] = current_well.index_no
    #
    #     record_start = model.objects.order_by('date').first().date
    #     record_end = model.objects.order_by('date').last()
    #     ctx['defaultstart'] = record_start
    #     ctx['defaultend'] = record_end.date
    #     ctx['lastreading'] =record_end.reading
    #
    #     ctx['readings'] = model.objects.all().order_by('-date')
    #     welljson = ctx['readings'][:12]
    #     wellgraph = []
    #     for reading in welljson:
    #         date = reading.date.strftime('%m/%d/%Y')
    #         depth = str(reading.reading)
    #         welldict = {"x":date, "y":depth}
    #         wellgraph.append(welldict)
    #     ctx['welljson'] = json.dumps(wellgraph)
    #
    #     return ctx

class WellQueryTemplateView(TemplateView):
    template_name = 'groundwater_app/query.html'

    def get_context_data(self, **kwargs):
        ctx = super(WellQueryTemplateView, self).get_context_data(**kwargs)
        well_name = self.request.session['wellname']
        model = apps.get_model('groundwater_app', well_name)
        ctx['name'] = well_name
        ctx['index_no'] = self.request.session['index_no']
        record_start = model.objects.order_by('date').first().date
        record_end = model.objects.order_by('date').last()
        ctx['defaultstart'] = record_start
        ctx['defaultend'] = record_end.date

        if self.request.GET.get('startdate') and self.request.GET.get('enddate'):
            startdate = self.request.GET.get('startdate')
            enddate = self.request.GET.get('enddate')
            ctx['startdate'] = datetime.strptime(startdate, '%Y-%m-%d')
            ctx['enddate'] = datetime.strptime(enddate, '%Y-%m-%d')

            ctx['readings'] = model.objects.filter(date__range=[startdate, enddate])

        return ctx

class ReadingCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = WellForm
    template_name = 'groundwater_app/create_reading.html'

    #Get model
    def get(self, request, *args, **kwargs):
        current_well = Well.objects.get(index_no=self.kwargs['pk'])
        well_name = current_well.name.replace(' ', '')
        self.model = apps.get_model('groundwater_app', well_name)
        return super(ReadingCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ReadingCreateView, self).get_context_data(**kwargs)
        ctx['name'] = self.request.session['name']
        ctx['index_no'] = self.kwargs['pk']
        return ctx

    def post(self, request, *args, **kwargs):
        current_well = Well.objects.get(index_no=self.kwargs['pk'])
        well_name = current_well.name.replace(' ', '')
        self.model = apps.get_model('groundwater_app', well_name)
        return super(ReadingCreateView, self).post(request, *args, **kwargs)
