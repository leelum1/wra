from django.conf.urls import url
from . import views

app_name = 'data_app'

urlpatterns=[
    url(r'^gauges/$', views.GaugeListView.as_view(), name='gaugelist'),
    url(r'^readers/$', views.GaugeReaderView.as_view(), name='readers'),
    url(r'^gaugedetail/(?P<pk>\S+)/$',views.GaugeDetailView.as_view(),name='gaugedetail'),
    url(r'^addrainfall/$', views.addRainfall, name='addrainfall'),
    url(r'^IDF/(?P<pk>\w+\.\w+)/$', views.IDFView.as_view(), name='IDF'),
    url(r'^gauge_compare/$', views.CompareTemplateView.as_view(), name='compare'),
]
