from django.shortcuts import *
from django.views import generic
from .models import *

# Create your views here.


class HomeView(generic.ListView):
    template_name = 'Marketplace/home.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        return Item.objects.all()

def ProfileView(request, user_id):
    user = get_object_or_404(Profile, pk = user_id)
    items = list(Item.objects.filter(profile = user_id))

    return render(request, 'Marketplace/profile.html', {'user': user, 'items':items})

def ItemDetailsView(request, user_id):
    item = get_object_or_404(Item, pk=user_id)
    return render(request, 'Marketplace/details.html', {'item': item})