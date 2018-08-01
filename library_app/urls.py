from django.conf.urls import url
from . import views

app_name = 'library_app'

urlpatterns=[
    url(r'^$',views.LibraryTemplateView.as_view(), name='library'),
    url(r'^booklist/$', views.BookListView.as_view(), name='booklist'),
    url(r'^book/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name="book-detail"),
    url(r'^SOP/$', views.SOPTemplateView.as_view(), name='sop'),
    url(r'^SOP/(?P<slug>\S+)/$', views.SOPDetailView.as_view(), name="sop-detail"),
]
