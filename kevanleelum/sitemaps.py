from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from watershed_app.models import Watershed

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['index',
                'legal',
                'data',
                'iwrm',
                'contact',
                'library_app:library',
                'map_app:map',
                'rivers_app:list',
                'reservoir_app:reservoir',
                'spi_app:SPI',
                'watershed_app:watersheds']

    def location(self, item):
        return reverse(item)

class WatershedSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Watershed.objects.all()

    def location(self, item):
        return reverse('watershed_app:detail', args=[str(item.slug)])
