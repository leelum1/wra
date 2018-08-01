from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from .decorators import management_required
from .models import Computer, Vehicle
from data_app.models import RainGauge
from streamflow_app.models import FuessGauge
from groundwater_app.models import Well

# Create your views here.
@method_decorator([management_required,], name='dispatch')
class AssetTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'asset_app/asset.html'

    def get_context_data(self, **kwargs):
        ctx = super(AssetTemplateView, self).get_context_data(**kwargs)
        ctx['raincount'] = RainGauge.objects.all().count
        ctx['fuesscount'] = FuessGauge.objects.all().count
        ctx['wellcount'] = Well.objects.all().count

        ctx['computers'] = Computer.objects.filter(needs_attn=True)
        ctx['vehicles'] = Vehicle.objects.filter(needs_attn=True)
        ctx['raingauges'] = RainGauge.objects.filter(needs_attn=True)
        ctx['fuess'] = FuessGauge.objects.filter(needs_attn=True)
        ctx['wells'] = Well.objects.filter(needs_attn=True)

        ctx['rainattncount'] = ctx['raingauges'].count
        ctx['fuessattncount'] = ctx['fuess'].count
        ctx['wellsattncount'] = ctx['wells'].count

        return ctx

@method_decorator([management_required,], name='dispatch')
class ComputerListView(LoginRequiredMixin, ListView):
    model = Computer
    template_name = 'asset_app/it_list.html'
    context_object_name = "computers"

@method_decorator([management_required,], name='dispatch')
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'asset_app/vehicle_list.html'
    context_object_name = "vehicles"
