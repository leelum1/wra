from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from data_app.models import RainGauge
from groundwater_app.models import Well
from streamflow_app.models import MeteringSite
from .forms import ContactForm

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class DataView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        ctx = super(DataView, self).get_context_data(**kwargs)
        ctx['rain'] = RainGauge.objects.all().count
        ctx['wells'] = Well.objects.all().count
        ctx['rivers'] = MeteringSite.objects.all().count
        return ctx

class LegalTemplateView(TemplateView):
    template_name = 'legal.html'

class IWRMTemplateView(TemplateView):
    template_name = 'iwrm.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        if self.request.is_ajax():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            send_mail('Website Query from ' + name, message + "\n\nReply to " + name + " at " + email, 'queries@waterresourcestt.com', ['kevanleelum@gmail.com',],
                fail_silently=False,
            )
            return JsonResponse({"message": "Your message has bean sent. Returning to the home page now..."})
        return super().form_valid(form)

def google_verify(request):
    return render(request, 'googlea70085b6066e71d7.html')
