from menu import Menu
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.menu = Menu()
        self.resources = {
            "water": 1000,
            "milk": 500,
            "coffee": 300,
            "tea_seeds": 100,
            "sugar": 600
        }

    def is_resource_sufficient(self, drink, asking_sugar, doubled):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if doubled == "Half":
            drink.cost["Dollar"] = drink.cost["Dollar"] / 2
            drink.cost["Lira"] = drink.cost["Lira"] / 2
            for ingredient in drink.ingredients:
                drink.ingredients[ingredient] = drink.ingredients[ingredient] / 2
        elif doubled == "Double":
            drink.cost["Dollar"] = drink.cost["Dollar"] * 2
            drink.cost["Lira"] = drink.cost["Lira"] * 2
            for ingredient in drink.ingredients:
                drink.ingredients[ingredient] = drink.ingredients[ingredient] * 2
        if asking_sugar == "without sugar".lower():
            drink.ingredients["sugar"] = 0
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                can_make = False
        # print(self.menu.find_drink(name).cost)
        # print(drink.ingredients)
        return can_make

    def make_coffee(self, order, heated, asking_sugar, doubled):
        """Deducts the required ingredients from the resources."""

        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        if heated == "Hot" and asking_sugar == "with sugar".lower() and doubled == "Normal":
            return f"Here is your Hot with sugar ", f"Normal {order.name}  ☕️. Enjoyy!"
        elif heated == "Cold" and asking_sugar == "with sugar".lower() and doubled == "Normal":
            return f"Here is your Cold with sugar ", f"Normal {order.name} ☕️. Enjoyy!"
        elif heated == "Hot" and asking_sugar == "without sugar".lower() and doubled == "Normal":
            return f"Here is your Hot without sugar", f" Normal {order.name} ☕️. Enjoyy!"
        elif heated == "Cold" and asking_sugar == "without sugar ".lower() and doubled == "Normal":
            return f"Here is your Cold without sugar", f"Normal {order.name} ☕️. Enjoyy!"
        elif heated == "Hot" and asking_sugar == "with sugar".lower() and doubled == "Half":
            return f"Here is your Hot with sugar", f"Half {order.name}  ☕️. Enjoyy!"
        elif heated == "Cold" and asking_sugar == "with sugar".lower() and doubled == "Half":
            return f"Here is your Cold with sugar", f" Half {order.name} ☕️. Enjoyy!"
        elif heated == "Hot" and asking_sugar == "without sugar".lower() and doubled == "Half":
            return f"Here is your Hot without sugar", f" Half {order.name} ☕️. Enjoyy!"
        elif heated == "Cold" and asking_sugar == "without sugar".lower() and doubled == "Half":
            return f"Here is your Cold without sugar", f"Half {order.name} ☕️. Enjoyy!"
        elif heated == "Hot" and asking_sugar == "with sugar".lower() and doubled == "Double":
            return f"Here is your Hot with sugar ", f"Double {order.name}  ☕️. Enjoyy!"
        elif heated == "Cold" and asking_sugar == "with sugar".lower() and doubled == "Double":
            return f"Here is your Cold with sugar", f" Double {order.name} ☕️. Enjoyy!"
        elif heated == "Hot" and asking_sugar == "without sugar".lower() and doubled == "Double":
            return f"Here is your Hot without sugar ", f"Double {order.name} ☕️. Enjoyy!"
        elif heated == "Cold" and asking_sugar == "without sugar".lower() and doubled == "Double":
            return f"Here is your Cold without sugar ", f"Double {order.name} ☕️. Enjoyy!"
