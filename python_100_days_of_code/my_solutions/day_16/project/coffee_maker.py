class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffe: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        
        return True
    
    def make_coffee(self, order):
        for ingredient in order.ingredients:
            self.resources[ingredient] -= order.ingredients[ingredient]