from django.views.generic import TemplateView, CreateView
from .models import Caroni, Navet, Hollis, Hillsborough
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

class ReservoirTemplateView(TemplateView):
    template_name = 'reservoir_app/reservoir.html'

    def get_context_data(self, **kwargs):
        ctx = super(ReservoirTemplateView, self).get_context_data(**kwargs)
        # Caroni
        current_date = Caroni.objects.order_by('date').last().date
        caronijson = []
        for x in range(1,13):
            current_year = datetime.strftime(current_date, '%Y')
            current_month = datetime.strftime(current_date, '%m')
            end_month = Caroni.objects.filter(date__year=current_year,
                                                    date__month=current_month).last()
            date = end_month.date.strftime('%m/%d/%Y')
            level = str(end_month.level)
            leveldict = {"x":date, "y":level}
            caronijson.append(leveldict)
            current_date -= relativedelta(months=1)
        ctx['caroni'] = json.dumps(caronijson)

        # Navet
        current_date = Navet.objects.order_by('date').last().date
        navetjson = []
        for x in range(1,13):
            current_year = datetime.strftime(current_date, '%Y')
            current_month = datetime.strftime(current_date, '%m')
            end_month = Navet.objects.filter(date__year=current_year,
                                                    date__month=current_month).last()
            date = end_month.date.strftime('%m/%d/%Y')
            level = str(end_month.level)
            leveldict = {"x":date, "y":level}
            navetjson.append(leveldict)
            current_date -= relativedelta(months=1)
        ctx['navet'] = json.dumps(navetjson)

        # Hollis
        current_date = Hollis.objects.order_by('date').last().date
        hollisjson = []
        for x in range(1,13):
            current_year = datetime.strftime(current_date, '%Y')
            current_month = datetime.strftime(current_date, '%m')
            end_month = Hollis.objects.filter(date__year=current_year,
                                                    date__month=current_month).last()
            date = end_month.date.strftime('%m/%d/%Y')
            level = str(end_month.level)
            leveldict = {"x":date, "y":level}
            hollisjson.append(leveldict)
            current_date -= relativedelta(months=1)
        ctx['hollis'] = json.dumps(hollisjson)

        # Hillsborough
        current_date = Hillsborough.objects.order_by('date').last().date
        hillsboroughjson = []
        for x in range(1,13):
            current_year = datetime.strftime(current_date, '%Y')
            current_month = datetime.strftime(current_date, '%m')
            end_month = Hillsborough.objects.filter(date__year=current_year,
                                                    date__month=current_month).last()
            date = end_month.date.strftime('%m/%d/%Y')
            level = str(end_month.level)
            leveldict = {"x":date, "y":level}
            hillsboroughjson.append(leveldict)
            current_date -= relativedelta(months=1)
        ctx['hillsborough'] = json.dumps(hillsboroughjson)
        return ctx

class CaroniTemplateView(TemplateView):
    template_name = 'reservoir_app/caroni.html'

class CaroniCreateView(CreateView):
    model = Caroni
    template_name = 'reservoir_app/caroni_create.html'
    fields = ['date', 'rainfall', 'level', 'production',]

class NavetTemplateView(TemplateView):
    template_name = 'reservoir_app/navet.html'

class NavetCreateView(CreateView):
    model = Navet
    template_name = 'reservoir_app/navet_create.html'

class HollisTemplateView(TemplateView):
    template_name = 'reservoir_app/hollis.html'

class HollisCreateView(CreateView):
    model = Hollis
    template_name = 'reservoir_app/hollis_create.html'

class HillsboroughTemplateView(TemplateView):
    template_name = 'reservoir_app/hillsborough.html'

class HillsboroughCreateView(CreateView):
    model = Hillsborough
    template_name = 'reservoir_app/hillsborough_create.html'
