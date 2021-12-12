from django.test import TestCase
import unittest
from app.models import Supplier, Product
from app.views import supplierlistview, productlistview
from .laskin import plus
from django.test import Client
from django.urls import reverse
client = Client()

# setUp metodi testiluokan alussa määrittää jonkin toimenpiteen tekemisen ennen jokaista jäljempänä määritettyä testiä.

class SupplierModelTests(TestCase):
    def setUp(self):
        Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", address="Kultatie 1", phone="12345567", email="jaakko@kulta.fi", country="Finland")
        
    def test_added_supplier_exists(self):
        """Added supplier exists and can be searched"""
        supplier = Supplier.objects.get(companyname="Test company")
        self.assertEqual(supplier.address, "Kultatie 1")
        self.assertEqual(supplier.country, "Finland")
        self.assertEqual(supplier.phone, "12345567")


class ProductModelTests(TestCase):
    def setUp(self):
        x = Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", address="Kultatie 1", phone="12345567", email="jaakko@kulta.fi", country="Finland")
        Product.objects.create(productname="Hillo", packagesize="300g", unitprice=4.1, unitsinstock=100, supplier=x)
        
    def test_added_product_exists(self):
        """Added product exists and can be searched"""
        product = Product.objects.get(unitprice=4.1)
        self.assertEqual(product.productname, "Hillo")


class UserAuthTests(TestCase):
    def test_listing_products(self):
        '''Call to product list url returns statuscode 200 but let not enter in'''
        response = client.get(reverse(productlistview))
        self.assertEqual(response.status_code, 200)
        a = False
        content = str(response.content)
        if (content.find("login") > 0):
            a = True
        self.assertEqual(a, True)
        

    def test_listing_suppliers(self):
        '''Call to supplier list url returns statuscode 200 but let not enter in'''
        response = client.get(reverse(supplierlistview))
        self.assertEqual(response.status_code, 200)
        a = False
        content = str(response.content)
        if (content.find("login") > 0):
            a = True
        self.assertEqual(a, True)


class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual:
        self.assertEqual(plus(7, 2), 9)

    def test_plus_string(self):
        # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual:
        self.assertEqual(plus("700", "200"), 900)
    #Jos laittaa väärän luvun, niin ilmoittaa failuresta ja syyn!

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 3), "teppo")
