from django.urls import path

from app.views import landingview
from .views import landingview, productlistview, supplierlistview, addsupplier

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]
