from django.conf.urls import url
from . import views

app_name = "reservoir_app"

urlpatterns = [
    url(r'^$', views.ReservoirTemplateView.as_view(), name='reservoir'),
    url(r'^Caroni/$', views.CaroniTemplateView.as_view(), name='caroni'),
    url(r'^Caroni/add/$', views.CaroniCreateView.as_view(), name='caronicreate'),
    url(r'^Navet/$', views.NavetTemplateView.as_view(), name='navet'),
    url(r'^Navet/add/$', views.NavetCreateView.as_view(), name='navetcreate'),
    url(r'^Hollis/$', views.HollisTemplateView.as_view(), name='hollis'),
    url(r'^Hollis/add/$', views.HollisCreateView.as_view(), name='holliscreate'),
    url(r'^Hillsborough/$', views.HillsboroughTemplateView.as_view(), name='hillsborough'),
    url(r'^Hillsborough/add/$', views.HillsboroughCreateView.as_view(), name='hillsboroughcreate'),
]
