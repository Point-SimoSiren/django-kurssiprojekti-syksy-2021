from django.test import TestCase
import unittest

from .laskin import plus

class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein
        self.assertEqual(plus(7, 2), 9)
    def test_plus_string(self):
        # testaa että numerot lasketaan yhteen oikein
        self.assertEqual(plus("700", "400"), 1100)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 3), "teppo")
