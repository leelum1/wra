from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,
                                CreateView, UpdateView, DeleteView)

# Create your views here.
class QualityTemplateView(TemplateView):
    template_name = 'quality_app/quality.html'
