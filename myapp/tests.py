from django.test import TestCase
from .utils import predict_price

class PricePredictionTests(TestCase):
    def test_price_increase(self):
        self.assertEqual(predict_price(10, 40, True, True), 15)

    def test_price_no_increase(self):
        self.assertEqual(predict_price(10, 50, False, False), 10)