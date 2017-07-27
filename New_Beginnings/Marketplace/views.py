from django.shortcuts import render
from django.views import generic
from .models import Item
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'Marketplace/home.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        return Item.objects.all()