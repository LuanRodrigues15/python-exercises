MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300, #300
    "milk": 200, #200
    "coffee": 100, # 100
    "profit" : 0
}

def check_resources(drink):
    for ingredient in drink:
        if drink[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quartes = (int(input("how many quarters?: ")) * 0.25)  # 0.25
    dimes = (int(input("how many dimes?: ")) * 0.10)      # 0.10
    nickles = (int(input("how many nickles?: ")) * 0.05)  # 0.05
    pennies = (int(input("how many pennies?: ")) * 0.01)  # 0.01
    total_money = quartes + dimes + nickles + pennies

    return total_money

def check_transaction(order, money):
    if order > money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if order < money:
            print(f"Here is ${round(money - order, 2)} dollars in change.")
        
        resources["profit"] += order
        return True

def make_coffe(drink, order):
    for ingredient in drink:
        resources[ingredient] -= drink[ingredient]
    
    print(f"Here is your {order}. Enjoy!")

# -------------------------------------------------------------------------------------------------------------
print("The Coffe Machine ☕")

coffe_machine = True

while coffe_machine:
    order = input("What would you like? (espresso {e} / latte {l} / cappuccino) {c}: ").lower()

    if order == "off":
        print("The Coffe Machine was switched off.")
        break
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ${resources['profit']}\n")
        
    else:
        match order:
            case "e":
                order = "espresso"
            case "l":
                order = "latte"
            case "c":
                order = "cappuccino"
            case _:
                print("Invalid option")
                continue
        
        drink = MENU[order]

        has_resources = check_resources(drink["ingredients"])
        if has_resources:
            has_checked = check_transaction(drink["cost"], process_coins())
            if has_checked:
                make_coffe(drink["ingredients"], order)