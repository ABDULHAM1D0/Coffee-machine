class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, sugar, tea, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "tea_seeds": tea,
            "sugar": sugar
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, tea=0, sugar=20, cost={"Dollar": 3, "Lira": 115}),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, tea=0, sugar=20, cost={"Dollar": 3.5, "Lira": 130}),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, tea=0, sugar=20, cost={"Dollar": 5, "Lira": 160}),
            MenuItem(name="choy", water=100, milk=0, coffee=0, tea=10, sugar=20, cost={"Dollar": 2, "Lira": 65}),
            MenuItem(name="qora cofe", water=150, milk=0, coffee=30, tea=0, sugar=15, cost={"Dollar": 3, "Lira": 115}),

        ]

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
