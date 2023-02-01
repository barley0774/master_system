from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザ名'})
            self.fields['username'].label = False
            self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'パスワード'}) 
            self.fields['password'].label = False