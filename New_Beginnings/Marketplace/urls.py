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
    url(r'^post/$', views.PostItemView.as_view() ,name = 'post'),
    url(r'^offer/(?P<item_id>[0-9]+)/$', views.MakeOfferView.as_view() ,name = 'offer'),
    url(r'^delete/(?P<offer_id>[0-9]+)/$', views.delete ,name = 'delete'),
    url(r'^update/(?P<item_id>[0-9]+)/(?P<offer_id>[0-9]+)/$', views.update.as_view() ,name = 'update'),
    url(r'^decline/(?P<user_id>[0-9]+)/(?P<offer_id>[0-9]+)/$', views.decline.as_view() ,name = 'decline'),
    url(r'^accept/(?P<user_id>[0-9]+)/(?P<item_id>[0-9]+)/(?P<offer_id>[0-9]+)/$', views.accept.as_view() ,name = 'accept')
]
