from django.urls import path

from .views import landingview, productlistview, supplierlistview

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),

    # Supplier url´s
    path('suppliers/', supplierlistview),
]
