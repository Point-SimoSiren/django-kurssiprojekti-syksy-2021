from django.test import TestCase
import unittest

from .laskin import plus

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