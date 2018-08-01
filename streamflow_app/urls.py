from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

app_name = 'streamflow_app'

urlpatterns = [
    url(r'^fuess_gauges/$', views.FuessListView.as_view(), name='fuess_list'),
    url(r'^meterings/$', views.MeteringListView.as_view(), name='metering_list'),
    url(r'^meterings/detail/(?P<pk>\d+\.\d+)/$',views.MeteringDetailView.as_view(),name='metering_detail'),
    url(r'^meterings/add/(?P<pk>\d+\.\d+)/$',views.MeteringCreateView.as_view(),name='add_metering'),
    url(r'^recession/(?P<pk>\d+\.\d+)/$', views.RecessionTemplateView.as_view(), name='recession'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
