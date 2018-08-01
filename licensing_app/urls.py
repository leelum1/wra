from django.conf.urls import url
from . import views

app_name = 'licensing_app'

urlpatterns = [
    url(r'^$', views.LicensingView.as_view(), name='licensing'),
    url(r'^licensing_detail/$', views.LicensingDetailView.as_view(), name='detail'),
    url(r'^apply/$', views.LicenseFormView.as_view(), name='apply'),
]
