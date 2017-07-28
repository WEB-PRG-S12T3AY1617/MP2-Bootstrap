from django.shortcuts import *
from django.views import generic
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.


def HomeView(request):
    all_items_list = Item.objects.all()
    template_name = 'Marketplace/home.html'
    context_object_name = 'all_items'
    paginator = Paginator(all_items_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        all_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_items = paginator.page(paginator.num_pages)

    return render(request, 'Marketplace/home.html', {'all_items':all_items})

def ProfileView(request, user_id):
    user = get_object_or_404(Profile, pk = user_id)
    items = list(Item.objects.filter(profile = user_id))

    return render(request, 'Marketplace/profile.html', {'user': user, 'items':items})

def ItemDetailsView(request, user_id):
    item = get_object_or_404(Item, pk=user_id)
    return render(request, 'Marketplace/details.html', {'item': item})
