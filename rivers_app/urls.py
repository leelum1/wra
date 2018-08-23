from django.conf.urls import url
from . import views

app_name = 'rivers_app'

urlpatterns = [
    url(r'^$', views.RiversListView.as_view(), name='list'),
]
