import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Mocha", 33, 5)
        self.drink2 = Drink("Latte", 35, 4)
        self.drink3 = Drink("Hot Chocolate", 24, 0)
        self.drink4 = Drink("Tea", 30, 4)
        self.drinks = [self.drink1, self.drink2, self.drink3, self.drink4]
        self.coffee_shop = CoffeeShop("Starbucks", 100, self.drinks)
        self.customer = Customer("Garry", 700, 20, 15)
    
    def test_coffee_shop_has_name(self):
        # "Starbucks" == self.coffee_shop.name
        self.assertEqual("Starbucks", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_increase_till(self):
        self.coffee_shop.increase_till(10)
        self.assertEqual(110, self.coffee_shop.till)

    def test_sell_drink(self):
        self.coffee_shop.sell_drink(self.drink1, self.customer)
        self.assertEqual(133, self.coffee_shop.till)