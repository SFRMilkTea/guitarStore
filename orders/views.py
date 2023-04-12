from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from .tasks import *
from cart.cart import Cart
from orders.models import Order
from .forms import OrderCreateForm
from .models import OrderItem


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
                                             address=address,
                                             first_name=user.first_name,
                                             last_name=user.last_name,
                                             email=user.email,
                                             )
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                # запуск асинхронной задачи
                order_created.delay(order.id)
                return render(request, 'orders/order/created.html',
                              {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'orders/order/create.html',
                      {'cart': cart, 'form': form})

    def order_detail(request, id_order):
        order = get_object_or_404(Order, id=id_order)
        return render(request, 'orders/order/detail.html',
                      {'order': order})


class OrderItemsListView(ListView):
    template_name = 'order/detail.html'
    model = OrderItem
    context_object_name = "list_of_all_order_items"
