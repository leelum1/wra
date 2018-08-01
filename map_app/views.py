from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.
class MapTemplateView(TemplateView):
    template_name = 'map_app/map.html'

    def get_context_data(self, **kwargs):
        ctx = super(MapTemplateView, self).get_context_data(**kwargs)
        ctx['MAPBOX_TOKEN'] = settings.MAPBOX_TOKEN
        return ctx
