import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Gary", 700, 20, 15)


    def test_customer_has_name(self):
        self.assertEqual("Gary", self.customer.name)


    def test_customer_has_wallet(self):
        self.assertEqual(700, self.customer.wallet)
    

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(35)
        self.assertEqual(665, self.customer.wallet)
