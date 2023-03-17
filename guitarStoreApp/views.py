from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from cart.forms import CartAddProductForm
from guitarStoreApp.models import Product, Producer


class HomePageView(TemplateView):
    template_name = 'home.html'


class GuitarListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = "list_of_all_products"


class GuitarView(TemplateView):

    template_name = 'product/detail.html'
    model = Product
    context_object_name = "product"

    def product_detail(request, id_product):
        product = get_object_or_404(Product, id_product=id_product)
        cart_product_form = CartAddProductForm()
        return render(request, 'product/detail.html',
                      {'product': product, 'cart_product_form': cart_product_form})


class ProducersListView(ListView):
    template_name = 'producers.html'
    model = Producer
    context_object_name = "list_of_all_producers"


class SearchView(ListView):
    template_name = 'search.html'
    model = Product
    context_object_name = "list_of_all_products"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(id_producer__producer__icontains=query)).reverse()


def product_detail(request, id_product):
    product = get_object_or_404(Product,
                                id_product=id_product,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product,
                                                   'cart_product_form': cart_product_form})
