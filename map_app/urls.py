from django.conf.urls import url
from . import views

app_name = 'map_app'

urlpatterns = [
    url(r'^$',views.MapTemplateView.as_view(), name='map'),
]
