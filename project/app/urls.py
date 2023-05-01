from django.urls import path
from .views import *


urlpatterns = [
    path('', ServiceList.as_view(), name='service_list'),
    path('service/<int:service_id>', ServiceDetail.as_view(), name='service_detail'),
    path('service/payment/<int:service_id>', ServicePayment.as_view(), name='service_payment')
]
