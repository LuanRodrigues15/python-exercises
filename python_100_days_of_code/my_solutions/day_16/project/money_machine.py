class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        quartes = (int(input("how many quarters?: ")) * 0.25)  
        dimes = (int(input("how many dimes?: ")) * 0.10)      
        nickles = (int(input("how many nickles?: ")) * 0.05)  
        pennies = (int(input("how many pennies?: ")) * 0.01)  
        money = quartes + dimes + nickles + pennies
        
        return money

    def make_payment(self, cost):

        money = self.process_coins()

        if cost > money:
            return False
        else:
            if cost < money:
                print(f"Here is ${round(money - cost, 2)} dollars in change.")
            
            self.profit += cost
            return True