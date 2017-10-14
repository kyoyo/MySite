from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^author/$', views.AuthorCreateView.as_view(), name='author'),
    url(r'^book/$', views.AuthorCreateView.as_view(), name='book'),
]