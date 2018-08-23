from django.conf.urls import url
from . import views

app_name = 'spi_app'

urlpatterns=[
    url(r'^$', views.SPITemplateView.as_view(), name='SPI'),
]
