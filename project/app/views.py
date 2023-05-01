from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'app/index.html')


class ServiceList(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'app/index.html'

class ServiceDetail(DetailView):
    model = Service
    template_name = 'app/detail_service.html'
    pk_url_kwarg = 'service_id'
    context_object_name = 'service'


class ServicePayment(DetailView):
    model = Service
    template_name = 'app/service_payment.html'
    pk_url_kwarg = 'service_id'
    context_object_name = 'service'
