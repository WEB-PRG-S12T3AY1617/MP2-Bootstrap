from django.conf.urls import url
from . import views

app_name = 'Marketplace'

urlpatterns = [
    url(r'^$', views.HomeView, name='home'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.ProfileView, name='profile'),
    url(r'^item/(?P<user_id>[0-9]+)/$', views.ItemDetailsView, name='item'),
]