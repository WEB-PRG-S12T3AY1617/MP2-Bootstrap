from django.conf.urls import url
from . import views

app_name = 'Marketplace'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]