from django.conf.urls import url
from . import views

app_name = 'quality_app'

urlpatterns = [
    url(r'^$', views.QualityTemplateView.as_view(), name='quality'),
]
