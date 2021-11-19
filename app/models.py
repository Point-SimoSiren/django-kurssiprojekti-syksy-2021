from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="firma")
    contactname = models.CharField(max_length = 50, default="firma")
    address = models.CharField(max_length = 100, default="firma")
    phone = models.CharField(max_length = 20, default="firma")
    email = models.CharField(max_length = 50, default="firma")
    country = models.CharField(max_length = 50, default="firma")
    def __str__(self):
        return f"{self.companyname}, {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.productname}, {self.supplier.companyname}"
