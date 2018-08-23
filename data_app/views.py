from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from csv import reader
from json import dumps

from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.apps import apps
from django.db.models import Max, Sum, Q, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import RainGauge, GaugeReader
from .IDF_calc import *
from .stats_calc import *

class GaugeListView(ListView):
    model = RainGauge
    context_object_name = 'gauges'
    template_name = 'data_app/gauge_list.html'


class GaugeReaderView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = GaugeReader
    context_object_name = 'readers'
    template_name = 'data_app/readers.html'


class GaugeDetailView(DetailView):
    model = RainGauge
    template_name = 'data_app/gauge_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(GaugeDetailView, self).get_context_data(**kwargs)
        current_gauge = get_object_or_404(RainGauge, code=self.kwargs['pk'])
        gauge_name = current_gauge.name.replace(' ', '')
        get_model = apps.get_model('data_app', gauge_name)
        ctx['north'] = current_gauge.northing
        ctx['east'] = current_gauge.easting
        self.request.session['name'] = current_gauge.name
        self.request.session['code'] = current_gauge.code

        with open('rainstats.csv', 'r') as f:
          rainStatsList = list(reader(f))
          for gauge in rainStatsList:
              if gauge[0] == gauge_name:
                  ctx['statslist'] = gauge

        record_start = get_model.objects.order_by('date').first().date
        record_end = get_model.objects.order_by('date').last().date
        ctx['defaultstart'] = record_start
        ctx['defaultend'] = record_end
        self.request.session['defaultstart'] = str(record_start)
        self.request.session['defaultend'] = str(record_end)

        if self.request.GET.get('startdate') and self.request.GET.get('enddate'):
            startdate = self.request.GET.get('startdate')
            enddate = self.request.GET.get('enddate')
            ctx['startdate'] = datetime.strptime(startdate, '%Y-%m-%d')
            ctx['enddate'] = datetime.strptime(enddate, '%Y-%m-%d')

            #Daily Data
            if self.request.GET.get('datetype') == 'daily':
                ctx['dailyrecords'] = get_model.objects.filter(date__range=[startdate, enddate])

            #Monthly Data. Need to sum months and print month
            elif self.request.GET.get('datetype') == 'monthly':
                startyear = int(startdate[0:4])
                endyear = int(enddate[0:4])
                currentyear = startyear
                monthrainfall = []
                while currentyear < endyear + 1:
                    currentmonth = 1
                    monthlist = [currentyear]
                    while currentmonth < 13:
                        rainfall = get_model.objects.filter(date__year=currentyear,
                                                                date__month=currentmonth).aggregate(Sum('rainfall'))['rainfall__sum']
                        if rainfall != None: #rainfall has value
                            monthlist.append(rainfall)
                        else:
                            monthlist.append('-')
                        currentmonth += 1
                    monthrainfall.append(monthlist)
                    currentyear += 1
                ctx['monthlyrecords'] = monthrainfall

            #Annual Data. Need to sum years and print year
            elif self.request.GET.get('datetype') == 'annual':
                startyear = int(startdate[0:4])
                endyear = int(enddate[0:4])
                currentyear = startyear
                annualrainfall = []
                while currentyear < endyear + 1:
                    rainfall = get_model.objects.filter(date__year=currentyear).aggregate(Sum('rainfall'))['rainfall__sum']
                    if rainfall != None:
                        if int(rainfall) > 1000:
                            max_rain = get_model.objects.filter(date__year=currentyear).aggregate(Max('rainfall'))['rainfall__max']
                            inches = int(rainfall) * 0.0393701
                            annualtuple = (currentyear, rainfall, inches, max_rain)
                            annualrainfall.append(annualtuple)
                    currentyear += 1
                ctx['annualrecords'] = annualrainfall

        #For graph
        raingraph = []
        max_json = 0
        currentdate = record_end
        for x in range(0, 12):
            currentyear = datetime.strftime(currentdate, '%Y')
            currentmonth = datetime.strftime(currentdate, '%m')
            rain = get_model.objects.filter(date__year=currentyear,
                                                    date__month=currentmonth).aggregate(Sum('rainfall'))['rainfall__sum']
            if rain != None: #rainfall has value
                raindict = {"x":currentdate.strftime('%m/%d/%Y'), "y":rain}
                if rain > max_json:
                    max_json = rain
            else:
                raindict = {"x":currentdate.strftime('%m/%d/%Y'), "y":0}
            raingraph.append(raindict)
            currentdate -= relativedelta(months=1)
        ctx['rainjson'] = dumps(raingraph)
        ctx['max_json'] = dumps(max_json)

        return ctx


# To recalculate the rain stats, run: python rainStatsCalc()
# rainStatsCalc()


@login_required
def addRainfall(request):
    gauge_name = request.session['name'].replace(' ', '')
    model = apps.get_model('data_app', gauge_name) #model in question

    ctx = {} #context dictionary initialize
    ctx['name'] = request.session['name']
    ctx['code'] = request.session['code']

    if request.GET.get('startdate') and request.GET.get('enddate'):
        startdate = datetime.strptime(request.GET.get('startdate'), '%Y-%m-%d')
        enddate = datetime.strptime(request.GET.get('enddate'), '%Y-%m-%d')
        dates = []
        while startdate < enddate:
            dates.append(startdate)
            startdate += timedelta(days=1)
        dates.append(enddate)
        ctx['dates'] = dates

    else:
        date_list = [datetime.today() - timedelta(days=x) for x in range(0, 30)]
        ctx['dates'] = date_list[::-1]

    ctx['start'] = datetime.strptime(request.session['defaultstart'], '%Y-%m-%d')
    ctx['end'] = datetime.strptime(request.session['defaultend'], '%Y-%m-%d')


    if request.POST.get('newrain'):
        dates = request.POST.get('dates').split(",")
        newrain = request.POST.get('newrain').split(",")
        print(len(newrain))
        print(dates)
        objs = []

        for i in range(0, len(newrain)):
            obj = model(date=datetime.strptime(dates[i], '%d %b %Y').date().isoformat(),
                        rainfall=newrain[i])
            objs.append(obj)

        model.objects.bulk_create(objs)

        return render(request, 'data_app/gauge_list.html')

    return render(request, 'data_app/add_rainfall.html', ctx)

class CompareTemplateView(TemplateView):
    template_name = 'data_app/gauge_compare.html'

    def get_context_data(self, **kwargs):
        ctx = super(CompareTemplateView, self).get_context_data(**kwargs)
        ctx['gauges'] = RainGauge.objects.filter(category='Pot')

        if self.request.GET.get('gauge1') and self.request.GET.get('gauge2'):
            startdate = self.request.GET.get('startdate')
            gauge1 = RainGauge.objects.get(name=self.request.GET.get('gauge1'))
            gauge2 = RainGauge.objects.get(name=self.request.GET.get('gauge2'))
            gauge1_name = gauge1.name.replace(' ', '')
            gauge2_name = gauge2.name.replace(' ', '')
            record1 = apps.get_model('data_app', gauge1_name)
            record2 = apps.get_model('data_app', gauge2_name)

            ctx['date'] = datetime.strptime(startdate, '%Y-%m-%d')
            ctx['gauge1'] = gauge1
            ctx['gauge2'] = gauge2
            ctx['record1'] = record1.objects.get(date=startdate)
            ctx['record2'] = record2.objects.get(date=startdate)

        return ctx


class IDFView(TemplateView):
    template_name = 'data_app/IDFresult.html'

    def get_context_data(self, **kwargs):
        ctx = super(IDFView, self).get_context_data(**kwargs)
        current_gauge = get_object_or_404(RainGauge, code=self.kwargs['pk'])
        gauge_name = current_gauge.name.replace(' ', '')
        get_model = apps.get_model('data_app', gauge_name)
        ctx['name'] = current_gauge.name
        ctx['code'] = self.kwargs['pk']

        startyear = get_model.objects.order_by('date').first().date.year
        endyear = get_model.objects.order_by('date').last().date.year
        ctx['startyear'] = startyear
        ctx['endyear'] = endyear

        #get maximum rainfall every year
        rainfall = []
        for year in range(startyear,endyear):
            max_rain = get_model.objects.filter(date__year=year).aggregate(Max('rainfall'))['rainfall__max']
            if max_rain != None and max_rain > 30:
                rainfall.append(max_rain) #list of maximum values
        ctx['IDF'] = dur_freq(short_int(rainfall))
        ctx['DDF'] = dur_freq(ddf_int(rainfall))
        ctx['json_idf'] = dumps(ctx['IDF'])
        ctx['json_ddf'] = dumps(ctx['DDF'])

        return ctx
