from django.shortcuts import render
from django.views.generic import TemplateView

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderView(TemplateView):
    template_name = 'order/detail.html'
    model = Order
    context_object_name = "order"

    def order_create(request):
        cart = Cart(request)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                user = request.user
                address = form.cleaned_data['address']
                order = Order.objects.create(user=user,
                                             address=address)
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                return render(request, 'orders/order/created.html',
                              {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'orders/order/create.html',
                      {'cart': cart, 'form': form})
