from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.cart_detail, name='cart_detail'),
    path('cart_add/<int:id_product>/', CartView.cart_add, name='cart_add'),
    path('remove/<int:id_product>/', CartView.cart_remove, name='cart_remove'),
]
