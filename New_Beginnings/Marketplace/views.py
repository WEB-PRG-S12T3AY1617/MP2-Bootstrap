from django.shortcuts import *
from django.views import generic
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from Marketplace.forms import LoginForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import SignUpForm
from django.urls import reverse, reverse_lazy
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

    if request.user:
        current_user = request.user
    return render(request, 'Marketplace/home.html', {'all_items':all_items, 'current_user': current_user})

def ProfileView(request, user_id):
    user = get_object_or_404(Profile, pk = user_id)
    items = list(Item.objects.filter(profile = user_id))

    return render(request, 'Marketplace/profile.html', {'user': user, 'items':items})

def ItemDetailsView(request, user_id):
    item = get_object_or_404(Item, pk=user_id)
    return render(request, 'Marketplace/details.html', {'item': item})

def LoginView(request):
    username = "Not Logged In"
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
    else:
        loginForm = LoginForm()

    return render(request, 'Marketplace/login.html', {"username": username})

class UserFormView(generic.View):
    form_class = SignUpForm
    template_name = 'Marketplace/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('Marketplace/home.html')

        return render(request, self.template_name, {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.profile.birthdate = form.cleaned_data.get('birthdate')
            user.profile.is_Student = form.cleaned_data.get('Student')
            user.profile.degreeProgram = form.cleaned_data.get('degree')
            user.profile.office = form.cleaned_data.get('office')
            user.profile.FirstName = form.cleaned_data.get('first_name')
            user.profile.LastName = form.cleaned_data.get('last_name')
            user.save()
            user = authenticate(username=username, password = raw_password)
            login(request,user)
            return redirect('Marketplace:home')
    else:
        form = SignUpForm()

    return render(request, 'Marketplace/signup.html', {'form':form})

def logoutView(request):
    logout(request)