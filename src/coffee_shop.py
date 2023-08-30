class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink, customer):
        self.age_check(customer)
        self.energy_check(customer)
        customer.buy_drink(drink)
        self.increase_till(drink.price)
        
        
        

    def age_check(self, customer):
        if customer.age >= 16:
            return True
        else:
            return False

    def energy_check(self, customer):
        if customer.energy_level >= 20:
            return True
        else:
            return False
    

    
        




