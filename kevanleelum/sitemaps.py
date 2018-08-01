from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from watershed_app.models import Watershed

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['index', 'legal', 'data_app:data', 'library_app:library', 'map_app:map', 'watershed_app:watersheds']

    def location(self, item):
        return reverse(item)

class WatershedSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Watershed.objects.all()

    def location(self, item):
        return reverse('watershed_app:detail', args=[str(item.slug)])
