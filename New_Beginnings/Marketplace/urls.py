from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.views import logout


app_name = 'Marketplace'

urlpatterns = [

    url(r'^$', views.HomeView, name='home'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.ProfileView, name='profile'),
    url(r'^item/(?P<user_id>[0-9]+)/$', views.ItemDetailsView, name='item'),
    url(r'^login/$', auth_views.login, {'template_name': 'Marketplace/login.html'},name = 'login'),
    url(r'^loggedin/$', TemplateView.as_view(template_name='Marketplace/loggedin.html')),
    url(r'^signup/$', views.signup ,name = 'signup'),
    url(r'^logout/$', logout, {'next_page':'Marketplace:login'}, name = 'logout'),
]