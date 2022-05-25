from django import forms
from django.contrib.auth.models import User
from .models import MyUser

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email'}),
        label="メールアドレス")
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name':'password1'}),
        label="パスワード")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password2'}),
        label="パスワード(確認)")

    class Meta:
        model = MyUser
        fields = ['email','password1','password2']
        field_order = ['email','password1','password2']

