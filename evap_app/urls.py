from django.conf.urls import url
from . import views

app_name = 'evap_app'

urlpatterns = [
    url(r'^gauges/$', views.StationListView.as_view(), name='evap-list'),
    url(r'^gauge/(?P<pk>\d+\.\d+)/$',views.StationDetailView.as_view(),name='evap-detail'),
]
