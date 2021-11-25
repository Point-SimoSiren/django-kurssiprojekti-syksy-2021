from django.urls import path

from app.views import landingview
from .views import deletesupplier, landingview, productlistview, supplierlistview, deletesupplier, products_filtered
from .views import addsupplier, addproduct, deleteproduct, confirmdeleteproduct, confirmdeletesupplier
from .views import edit_product_post, edit_product_get, searchsuppliers

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('products-by-supplier/<int:id>/', products_filtered),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post), 
    

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('search-suppliers/', searchsuppliers),
]
