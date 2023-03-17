from django.contrib import admin
from django.urls import path, include

from cart.views import CartView

urlpatterns = [
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('', include('guitarStoreApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
