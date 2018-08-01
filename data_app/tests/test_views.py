from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import *

class DataPageTests(TestCase):
    def test_view_status_code(self):
        response = self.client.get('/data/')
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/data/')
        self.assertEquals(view.func.view_class, DataView)

    def test_uses_correct_template(self):
        response = self.client.get('/data/')
        self.assertTemplateUsed(response, 'data_app/data.html')
