from django.urls import path
from .views import OrderView

urlpatterns = [
    path('create/', OrderView.order_create, name='order_create'),
]
