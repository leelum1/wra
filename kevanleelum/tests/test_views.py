from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import *

class HomeTests(TestCase):
    def test_view_status_code(self):
        response = self.client.get('index')
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, IndexTemplateView)

    def test_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class LegalTests(TestCase):
    def test_view_status_code(self):
        response = self.client.get('legal')
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/legal/')
        self.assertEquals(view.func.view_class, LegalTemplateView)

    def test_uses_corect_template(self):
        response = self.client.get('/legal/')
        self.assertTemplateUsed(response, 'legal.html')

class ResumeTests(TestCase):
    def test_view_status_code(self):
        response = self.client.get('resume')
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/kevanleelum/')
        self.assertEquals(view.func.view_class, ResumeTemplateView)

    def test_uses_correct_template(self):
        response = self.client.get('/kevanleelum/')
        self.assertTemplateUsed(response, 'resume.html')
