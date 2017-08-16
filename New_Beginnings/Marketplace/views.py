from django.shortcuts import *
from django.views import generic
from django.views import View
from django.views.generic import TemplateView
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import *
from django.urls import reverse, reverse_lazy

def HomeView(request):
    all_items_list = Item.objects.all()
    template_name = 'Marketplace/home.html'
    context_object_name = 'all_items'
    query = request.GET.get("q")
    print(query)
    if query:
        all_items_list = all_items_list.filter(tag__text__icontains=query)
    paginator = Paginator(all_items_list, 10)
    page = request.GET.get('page')
    try:
        all_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_items = paginator.page(paginator.num_pages)

    if request.user.is_authenticated():
        current_user = request.user
        user_id = get_object_or_404(Profile, user = request.user).id
        offers = list(Offer.objects.all())
        return render(request, 'Marketplace/home.html', {'all_items':all_items, 'current_user': current_user, 'pk':user_id,'offers':offers})
    else:
        return render(request, 'Marketplace/home.html', {'all_items':all_items})

@login_required
def ProfileView(request, user_id):
    user = get_object_or_404(Profile, pk = user_id)
    items = list(Item.objects.filter(profile = user_id))
    query = request.GET.get("q")
    offers = list(Offer.objects.all())
    if query:
        return redirect('/Marketplace/?q=' + query + "#")
    return render(request, 'Marketplace/profile.html', {'user': user, 'items':items,'offers':offers})

def ItemDetailsView(request, user_id):
    item = get_object_or_404(Item, pk=user_id)
    if request.user.is_authenticated():
        id = get_object_or_404(Profile, user=request.user).id
        print("hello world")
        #print(get_object_or_404(Offer,item=get_object_or_404(Item,pk=user_id)))
        offers = list(Offer.objects.filter(item=get_object_or_404(Item,pk=user_id)))
        print(offers)
        return render(request, 'Marketplace/detailslogged.html', {'item': item, 'pk':id,'offers':offers})
    else:
        return render(request, 'Marketplace/details.html', {'item': item})

def LoginView(request):
    username = "Not Logged In"
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            user_id = request.user_id
    else:
        loginForm = LoginForm()

    return render(request, 'Marketplace/login.html', {"username": username})

class PostItemView(View):
    def get(self,request):
        postForm = PostItemForm()
        user_id = get_object_or_404(Profile, user = request.user).id
        context = {
            "title": "Hello world",
            "form": postForm,
            "pk":user_id
        }
        return render(request,'Marketplace/post.html',context)

    def post(self,request):
        postForm = PostItemForm(request.POST,request.FILES)
        if postForm.is_valid():
            temp = postForm.save(commit=False)
            temp.is_secondHand = 1
            temp.profile = get_object_or_404(Profile,user=request.user)
            temp.save()
            return redirect('Marketplace:home')
        else:
            print(postForm.errors.as_data())

        user_id = get_object_or_404(Profile, user = request.user).id
        return render(request, 'Marketplace/post.html', {'pk':user_id})

class MakeOfferView(View):
    def get(self,request,item_id):
        offerForm = MakeOfferForm()
        user_id = get_object_or_404(Profile, user = request.user).id
        offerForm.fields['item_offer'].queryset = Item.objects.filter(profile=get_object_or_404(Profile, user = request.user))
        print(get_object_or_404(Profile, user = request.user))
        context = {
            "form": offerForm,
            "pk": user_id
        }
        return render(request,'Marketplace/offer.html',context)
    def post(self,request,item_id):
        offerForm = MakeOfferForm(request.POST)
        if offerForm.is_valid():
            temp = offerForm.save(commit=False)
            temp.user = get_object_or_404(Profile,user=request.user)
            temp.item = get_object_or_404(Item,pk=item_id)
            temp.save()
            return redirect('Marketplace:home')
        else:
            print(offerForm.errors.as_data())

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

def delete(request,offer_id):
    Offer.objects.filter(pk=offer_id).delete()
    print("hello")
    return redirect('Marketplace:home')

class update(View):
    def get(self,request, item_id,offer_id):
        Offer.objects.filter(pk=offer_id).delete()
        offerForm = MakeOfferForm()
        user_id = get_object_or_404(Profile, user=request.user).id
        offerForm.fields['item_offer'].queryset = Item.objects.filter(
            profile=get_object_or_404(Profile, user=request.user))
        print(get_object_or_404(Profile, user=request.user))
        context = {
            "form": offerForm,
            "pk": user_id
        }
        return render(request, 'Marketplace/update.html', context)

    def post(self, request, item_id, offer_id):
        offerForm = MakeOfferForm(request.POST)
        if offerForm.is_valid():
            temp = offerForm.save(commit=False)
            temp.user = get_object_or_404(Profile, user=request.user)
            temp.item = get_object_or_404(Item, pk=item_id)
            temp.save()
            return redirect('Marketplace:home')
        else:
            print(offerForm.errors.as_data())

class decline(View):
    def get(self,request,user_id,offer_id):
        Offer.objects.filter(pk=offer_id).delete()
        return redirect('/Marketplace/profile/' + user_id + "/")
    def post(self,request,user_id,offer_id):
        return redirect('Marketplace/profile/' + user_id + "/")

class accept(View):
    def get(self,request,user_id,item_id,offer_id):
        Offer.objects.filter(pk=offer_id).delete()
        Item.objects.filter(pk=item_id).delete()
        return redirect('/Marketplace/profile/' + user_id + "/")
    def post(self,request,user_id,item_id,offer_id):
        return redirect('Marketplace/profile/' + user_id + "/")

