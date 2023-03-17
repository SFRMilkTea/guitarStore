from django.urls import path

from .views import HomePageView, GuitarListView, SearchView, GuitarView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/detail/<int:id_product>/', GuitarView.product_detail, name='product_detail'),
    path('products', GuitarListView.as_view(), name='products'),
    path('search', SearchView.as_view(), name='search'),
]
