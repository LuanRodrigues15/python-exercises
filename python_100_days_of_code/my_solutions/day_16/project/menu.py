from menu_item import MenuItem

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name = "espresso", cost = 1.5, ingredients = {"water" : 50, "coffee" : 18}),
            MenuItem(name = "latte", cost = 2.5, ingredients = {"water" : 200, "coffee" : 24, "milk" : 150}),
            MenuItem(name = "cappuccino", cost = 3.0, ingredients = {"water" : 250, "coffee" : 24, "milk" : 100}),
        ]
        

    def get_items(self):
        all_names = []

        for item in self.menu:
            all_names.append(item.name)

        all_names = "/".join(all_names)

        return all_names
           

    def find_drink(self, order_name):
        for item in self.menu:
            if order_name == item.name:
                return item
        return None