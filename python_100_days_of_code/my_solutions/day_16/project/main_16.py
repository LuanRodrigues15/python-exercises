from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    order_name = input(f"What would you like? ({menu.get_items()}): ").lower()

    if order_name == "off":
        print("Turn off the machine.")
        break
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
        print("")
    else:
        drink = menu.find_drink(order_name)
        if drink is None:
            print("Drink not found!")
            continue

        is_resources_sufficient = coffee_maker.is_resource_sufficient(drink)
        
        if is_resources_sufficient:
           check_transaction =  money_machine.make_payment(drink.cost)
           if check_transaction :
               coffee_maker.make_coffee(drink)
               print(f"Here is your {drink.name}. Enjoy!")