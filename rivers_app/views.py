from django.views.generic import ListView
from .models import River

# Create your views here.
class RiversListView(ListView):
    model = River
    template_name = 'rivers_app/rivers_list.html'
    context_object_name = 'rivers'
