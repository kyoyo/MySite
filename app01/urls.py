from django.conf.urls import url
from .views import LoginView,RegisterView
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^register/',RegisterView.as_view(),name='register'),
]