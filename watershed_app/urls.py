from django.conf.urls import url
from . import views

app_name = 'watershed_app'

urlpatterns = [
    url(r'^$', views.WatershedListView.as_view(), name="watersheds"),
    url(r'^(?P<slug>\S+)/$', views.WatershedDetailView.as_view(), name="detail"),
]
