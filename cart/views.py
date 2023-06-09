from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from guitarStoreApp.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartDeleteProductForm


class CartView(TemplateView):
    template_name = 'cart/detail.html'
    model = Cart
    context_object_name = "cart"

    @require_POST
    def cart_add(request, id_product):
        cart = Cart(request)
        product = get_object_or_404(Product, id_product=id_product)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=1,
                     update_quantity=cd['update'])
        return redirect('cart_detail')

    @require_POST
    def cart_delete(request, id_product):
        cart = Cart(request)
        product = get_object_or_404(Product, id_product=id_product)
        form = CartDeleteProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.delete(product=product,
                        quantity=1,
                        update_quantity=cd['update'])
        return redirect('cart_detail')

    def cart_remove(request, id_product):
        cart = Cart(request)
        product = get_object_or_404(Product, id_product=id_product)
        cart.remove(product)
        return redirect('cart_detail')

    def cart_detail(request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'update_quantity': True})
            item['update_quantity_form'] = CartDeleteProductForm(initial={'update_quantity': True})
        return render(request, 'cart/detail.html', {'cart': cart})
