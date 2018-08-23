"""kevanleelum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap, WatershedSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'watershed': WatershedSitemap,
}

urlpatterns = [
    url(r'^pie/doc/', include('django.contrib.admindocs.urls')),
    url(r'^pie/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^googlea70085b6066e71d7.html', views.google_verify, name='verify'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', views.IndexTemplateView.as_view(), name='index'),
    url(r'^data/$',views.DataView.as_view(),name='data'),
    url(r'^integrated-water-resources-management/$',views.IWRMTemplateView.as_view(),name='iwrm'),
    url(r'^contact/$', views.ContactFormView.as_view(), name='contact'),
    url(r'^legal/$', views.LegalTemplateView.as_view(), name='legal'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^assets/', include('asset_app.urls')),
    url(r'^blog/', include('blog_app.urls')),
    url(r'^rainfall/', include('data_app.urls')),
    url(r'^evaporation/', include('evap_app.urls')),
    url(r'^groundwater/', include('groundwater_app.urls')),
    url(r'^library/', include('library_app.urls')),
    url(r'^licensing/', include('licensing_app.urls')),
    url(r'^map/', include('map_app.urls')),
    url(r'^reservoirs/', include('reservoir_app.urls')),
    url(r'^rivers/', include('rivers_app.urls')),
    url(r'^waterquality/', include('quality_app.urls')),
    url(r'^spi/', include('spi_app.urls')),
    url(r'^streamflow/', include('streamflow_app.urls')),
    url(r'^watersheds/', include('watershed_app.urls')),
]

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
       url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
   ]
