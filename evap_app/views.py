from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Station

# Create your views here.
class StationListView(ListView):
    model = Station
    template_name = 'evap_app/evap_list.html'
    context_object_name = 'stations'

class StationDetailView(DetailView):
    model = Station
    template_name = 'evap_app/evap_detail.html'
    context_object_name = 'station'
