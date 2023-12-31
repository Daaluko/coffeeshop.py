import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mocha", 430, 5)


    def test_drink_has_name(self):
        self.assertEqual("Mocha", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(430, self.drink.price)
        