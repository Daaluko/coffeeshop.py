class Customer:
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        self.reduce_wallet(drink.price)
