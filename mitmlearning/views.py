from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from ipware import get_client_ip # クライアントのIP取得
from django.shortcuts import redirect # リダイレクト
from django.urls import reverse, reverse_lazy
from collections import defaultdict
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

import netifaces
import os


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views.generic import View

from .forms import TermForm

# 自作ファイル
from .mitm import rep_mitm, sniff_packet
# from .auto_login import login_box
from .models import Scenario, Term, Category
from .smail import smail

url_list = []
login_info = {}

# class ListTermView(ListView):
#     model = Term

#     template_name = 'mitmlearning/term.html'
class DetailTermView(DetailView):
    def get(self, request, *args, **kwargs):
        term_data = Term.objects.get(id=self.kwargs['pk'])
        return render(request, 'mitmlearning/term_detail.html', {'term_data':term_data})
    
class CreateTermView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TermForm(request.POST or None)
        return render(request, 'mitmlearning/term_create.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = TermForm(request.POST or None)
        
        if form.is_valid():
            term_data = Term()
            term_data.user = request.user
            term_data.term = form.cleaned_data['term']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            term_data.category = category_data
            term_data.text = form.cleaned_data['text']
            if request.FILES:
                term_data.image = request.FILES.get('image')
            term_data.save()
            return redirect('detail-term', term_data.id)
        
        return render(request, 'mitmlearning/term_create.html', {'form':form})
        
class DeleteTermView(LoginRequiredMixin, DeleteView):
    model = Term
    template_name = 'mitmlearning/term_delete.html'
    success_url = reverse_lazy('list-term')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj
    
class UpdateTermView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        term_data = Term.objects.get(id=self.kwargs['pk'])
        form = TermForm(
            request.POST or None,
            initial = {
                'term': term_data.term,
                'category': term_data.category,
                'text': term_data.text,
                'image': term_data.image,
            }
        )
        return render(request, 'mitmlearning/term_update.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = TermForm(request.POST or None)
        
        if form.is_valid():
            term_data = Term.objects.get(id=self.kwargs['pk'])
            term_data.term = form.cleaned_data['term']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            term_data.category = category_data
            term_data.text = form.cleaned_data['text']
            if request.FILES:
                term_data.image = request.FILES.get('image')
            term_data.save()
            return redirect('detail-term', self.kwargs['pk'])
        
        return render(request, 'mitmlearning/term_create.html', {'form':form})

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        client_addr, _ = get_client_ip(request)
        # デフォルトゲートウェイのIP
        gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
        category_data = Category.objects.get(name=self.kwargs['category'])
        term_data = Term.objects.order_by('-id').filter(category=category_data)
        context = {
            'term_data': term_data,
            'ip': client_addr,
            'gateway': gateway,
        }
        return render(request, 'mitmlearning/term_list.html', context)
    
def term_view(request):
    client_addr, _ = get_client_ip(request)
    # デフォルトゲートウェイのIP
    gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    term_data = Term.objects.order_by('-id')
    
    context = {
        'term_data': term_data,
        'ip': client_addr,
        'gateway': gateway,
    }
    return render(request, 'mitmlearning/term_list.html', context)

def index_view(request):
    client_addr, _ = get_client_ip(request)
    # デフォルトゲートウェイのIP
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]
    
    context = {
        'ip': client_addr,
        'gateway': gateway,
    }
    return render(request, 'mitmlearning/index.html',context)

def scenario(request):
    client_addr, _ = get_client_ip(request)
    # デフォルトゲートウェイのIP
    gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    
    scenario_block = Scenario.objects.order_by('order')
    content = {
        'scenario_block':scenario_block,
        'ip': client_addr,
        'gateway': gateway,
    }
    return render(request, 'mitmlearning/scenario.html', content)

def feedback(request):
    client_addr, _ = get_client_ip(request)
    print(client_addr)
    # デフォルトゲートウェイのIP
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]
    
    url_list, user_list, password_list = sniff_packet.sniff()
    
    zip_list = zip(user_list, password_list)
    
    content = {
        'ip': client_addr,
        'gateway': gateway,
        "url_list":url_list,
        "zip_list":zip_list,
    }
    return render(request, 'mitmlearning/feedback.html', content)

def sslstrip(request):
    client_addr, _ = get_client_ip(request)
    
    if request.method == 'POST':
        print(url_list)
        print(login_info)
        rep_mitm.sslstrip_around(client_addr)
    return redirect('index')

def dns_spoof(request):
    client_addr, _ = get_client_ip(request)
    if request.method == 'POST':
        print(url_list)
        print(login_info)
        rep_mitm.dns_spoof_around(client_addr)
    return redirect('index')
    
def stop_attack(request):

    rep_mitm.stop_attack()
    url_list, user_list, password_list = sniff_packet.sniff()
    
    zip_list = zip(user_list, password_list)
    
    return render(request, 'mitmlearning/feedback.html',{"url_list":url_list, "zip_list":zip_list})
    
def get_default_gateway(ip):
    for r in getattr(ip, 'routes', []):
        if r.get('subnet', '') == '0.0.0.0/0':
            return r.get('gateway', None)
    return None

def send_impersonation_email(request):
    if request.method == "POST":
        email = request.POST['impersonation_email']
        smail.send_email(email, 0)
        message = email + "にメールが正常に送信されました。"
        messages.success(request, message)
        return render(request, 'mitmlearning/feedback.html',)
    
def send_countermeasure_email(request):
    if request.method == "POST":
        email = request.POST['countermeasure_email']
        print(email)
        smail.send_email(email, 1)
        message = email + "にメールが正常に送信されました。"
        messages.success(request, message)
        return render(request, 'mitmlearning/term_list.html',)
    
def scenario_download_password(request, *args, **kwargs):
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/static/mitmlearning/file/password.txt"
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/plain")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

def scenario_download_credential(request, *args, **kwargs):
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/static/mitmlearning/file/dummy_pi1.csv"
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

# def auto_login(request):
#     login_box.auto_box_login()
#     return None

# def example_auto_login(request):
#     login_box.example_auto_login()
#     return redirect('feedback')
