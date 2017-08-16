from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class LoginForm(forms.Form):
    user= forms.CharField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    birthdate = forms.DateField(required=True, help_text='Required. Format: YYYY-MM-DD')
    Student = forms.BooleanField(required=False)
    degree = forms.CharField(max_length=30, required=False)
    office = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name' ,'birthdate','Student','degree','office','password1','password2',)

class PostItemForm(forms.ModelForm):
    item_name = forms.CharField()
    thumbnail = forms.FileField()
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    is_academic = forms.BooleanField(required=False)
    quantity = forms.IntegerField()
    course_name = forms.CharField()

    class Meta:
        model = Item
        fields = {'item_name','thumbnail','tag','is_academic','quantity','course_name'}

class MakeOfferForm(forms.ModelForm):
    is_Amount = forms.BooleanField(required=False)
    amount_offer = forms.IntegerField(required=False)
    reason = forms.CharField(required=True)

    class Meta:
        model = Offer
        fields = {'is_Amount','amount_offer','item_offer','reason'}