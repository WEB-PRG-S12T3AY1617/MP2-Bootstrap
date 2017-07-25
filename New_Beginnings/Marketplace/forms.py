from django import forms

class LoginForm(forms.Form):
    username = forms.charField(max_length = 50)
    password = forms.charField(widget = forms.PasswordInput())