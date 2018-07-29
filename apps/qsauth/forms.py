from django import forms
from apps.forms import FormMixin

class LoginForm(forms.Form,FormMixin):
    username = forms.CharField(max_length=11)
    password = forms.CharField(min_length=6)
    remember = forms.IntegerField(required=False)