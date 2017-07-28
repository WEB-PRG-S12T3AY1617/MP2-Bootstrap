from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
