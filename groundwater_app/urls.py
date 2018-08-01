from django.conf.urls import url
from . import views

app_name = 'groundwater_app'

urlpatterns = [
    url(r'^$', views.WellListView.as_view(), name='groundwater'),
    url(r'^detail/(?P<pk>\w+)/$',views.WellDetailView.as_view(),name='welldetail'),
    url(r'^detail/(?P<pk>\d+\.\d+)/query/$', views.WellQueryTemplateView.as_view(), name='wellquery'),
    url(r'^add/(?P<pk>\d+\.\d+)/$',views.ReadingCreateView.as_view(),name='create_reading'),
]
