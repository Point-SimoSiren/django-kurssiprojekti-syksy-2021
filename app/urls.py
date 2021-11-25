from django.urls import path

from app.views import landingview
from .views import deletesupplier, landingview, productlistview, supplierlistview, deletesupplier, products_filtered
from .views import addsupplier, addproduct, deleteproduct, confirmdeleteproduct, confirmdeletesupplier

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('products-by-supplier/<int:id>/', products_filtered),


    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
]
