from django.urls import path

from app.views import landingview
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, deleteproduct

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]
