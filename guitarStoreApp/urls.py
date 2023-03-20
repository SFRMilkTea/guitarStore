from django.urls import path

from .views import HomePageView, GuitarListView, SearchView, GuitarView, LkView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/detail/<int:id_product>/', GuitarView.product_detail, name='product_detail'),
    path('products', GuitarListView.as_view(), name='products'),
    path('lk', LkView.as_view(), name='lk'),
    path('search', SearchView.as_view(), name='search'),
]
