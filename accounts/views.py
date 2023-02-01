from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from  .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

#ログアウト機能の処理
class Logout(LogoutView):
    template_name = 'logout.html'