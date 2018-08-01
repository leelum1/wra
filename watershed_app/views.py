from django.views.generic import TemplateView, ListView, DetailView
from data_app.models import RainGauge
from streamflow_app.models import FuessGauge, MeteringSite
from groundwater_app.models import Well
from library_app.models import Book
from .models import Watershed

# Create your views here.
class WatershedListView(ListView):
    model = Watershed
    template_name = 'watershed_app/watershed_list.html'
    context_object_name = 'watersheds'

class WatershedDetailView(DetailView):
    model = Watershed
    template_name = 'watershed_app/watershed_detail.html'
    context_object_name = 'watershed'

    def get_context_data(self, **kwargs):
        ctx = super(WatershedDetailView, self).get_context_data(**kwargs)
        ctx['rainfall'] = RainGauge.objects.filter(watershed=self.get_object())
        ctx['fuess'] = FuessGauge.objects.filter(watershed=self.get_object())
        ctx['meterings'] = MeteringSite.objects.filter(watershed=self.get_object())
        ctx['library'] = Book.objects.filter(title__icontains=self.get_object())
        return ctx
