from django.conf.urls import url
from . import views

app_name = 'blog_app'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^create/$', views.PostCreateView.as_view(), name='create'),
    url(r'^update/(?P<slug>\S+)/$', views.PostUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<slug>\S+)/$', views.PostDeleteView.as_view(), name='delete'),
    url(r'^(?P<slug>\S+)/$', views.PostDetailView.as_view(), name='detail'),
]
