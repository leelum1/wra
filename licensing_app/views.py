from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .forms import AbstractionLicense
from asset_app.decorators import abstractor_required
from asset_app.models import User
# Create your views here.

class LicensingView(TemplateView):
    template_name = 'licensing_app/licensing.html'

@method_decorator([abstractor_required,], name='dispatch')
class LicensingDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'licensing_app/licensing_detail.html'

@method_decorator([abstractor_required,], name='dispatch')
class LicenseFormView(LoginRequiredMixin, FormView):
    login_url = 'login'
    template_name = 'licensing_app/licensing_form.html'
    form_class = AbstractionLicense
    success_url = 'licensing'
