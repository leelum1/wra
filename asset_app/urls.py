from django.conf.urls import url
from . import views

app_name = "asset_app"

urlpatterns = [
    url(r'^$', views.AssetTemplateView.as_view(), name="asset"),
    url(r'^computers/$', views.ComputerListView.as_view(), name="computer"),
    url(r'^vehicles/$', views.VehicleListView.as_view(), name="vehicle"),
]
