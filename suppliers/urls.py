from django.contrib import admin
from django.urls import path, include

# Jos lisää tämän niin saa helposti admin sivun otsikon oman näköiseksi
# ts. ei lue "Django admin"
admin.site.site_header = 'Suppliers app adminpage'
admin.site.site_title = 'Suppliers'
admin.site.index_title = 'Adminpage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
