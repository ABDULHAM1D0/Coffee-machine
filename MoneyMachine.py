from menu import Menu
class MoneyMachine:

    def __init__(self):
        self.profit = 0
        self.currencies = {"Dollar": "$",
                           "Lira": "₺", }
        self.menu = Menu()
        self.change = 0

    def process_currency(self, currency):
        for item in self.currencies:
            if currency == item:
                return self.currencies[item]

    # def calculating_money(self, currency, cofe):
    #     new_amount = 0
    #     if currency == "₺":
    #         new_amount = round(self.menu.get_items(cofe).cost * 31.83), 2
    #     return new_amount



    def make_payment(self, cost, currency, money_amount):
        """Returns True when payment is accepted, or False if insufficient."""
        if currency == "$":
            if int(money_amount) >= int(cost["Dollar"]):
                change = round(float(money_amount) - float(cost["Dollar"]), 2)
                self.profit += cost["Dollar"]
                self.change = change
                return True
            else:
                # print("Sorry that's not enough money. Money refunded.")
                return False
        elif currency == "₺":
            if int(money_amount) >= int(cost["Lira"]):
                change = round(float(money_amount) - float(cost["Lira"]), 2)
                self.profit += cost["Dollar"]
                self.change = change
                return True
            else:
                # print("Sorry that's not enough money. Money refunded.")
                return False

