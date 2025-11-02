from tkinter import *
from CoffeeMaker import CoffeeMaker
from menu import Menu
from MoneyMachine import MoneyMachine


window = Tk()
coffee_list = ["latte", "espresso", "cappuccino", "tea", "black coffee"]
temp_list = ["Hot", "Cold"]
size_list = ["Half", "Double", "Normal"]
currencies_list = ["Dollar", "Lira"]


coffee_maker = CoffeeMaker()
menu_coffee = Menu()
money_machine = MoneyMachine()
#--------------------------------------------Functions----------------------------------------#

sugar = 0
def showing_parts():
    global sugar
    enter_money.config(state="normal")
    coffee_name = coffee_order.get()
    size_name = size_order.get()
    sugar_name = radio_state.get()
    answer = menu_coffee.find_drink(coffee_name)
    sugar = menu_coffee.find_drink(coffee_name).ingredients["sugar"]

    if coffee_maker.is_resource_sufficient(answer, sugar_name, size_name):
        items_label.config(text="Sufficient ingredients")
    else:
        items_label.config(text="Insufficient ingredients ❌")
        enter_money.config(state="disabled")
    
    order_water_milk_amount.config(text=f"{answer.ingredients['water']} ml /"
                                            f"{answer.ingredients['milk']} ml")
    order_coffee_amount.config(text=f"{answer.ingredients['coffee']} g")
    order_tea_amount.config(text=f"{answer.ingredients['tea_seeds']} g")
    order_sugar_amount.config(text=f"{answer.ingredients['sugar']} g")
    order_cost_amount.config(text=f"{answer.cost['Dollar']} $/ "
                                      f"{answer.cost['Lira']} ₺")

def payment_fun():
    # this function make payment.
    currency_name = currency_order.get()
    coffee_name = coffee_order.get()
    amount_money = enter_money.get()
    name_currency = money_machine.process_currency(currency_name)
    if money_machine.make_payment(currency=name_currency, money_amount=amount_money,
                                  cost=menu_coffee.find_drink(coffee_name).cost):
        enter_money.delete(0, END)
        enter_money.config(state="disabled")
        payment_label.config(text=f"Change: {name_currency} {money_machine.change} ")
        product_works()
    else:
        payment_label.config(text="Insufficient Payment ❌")
        enter_money.config(state="normal")
    # print(money_machine.profit)
    # print(amount_money)


def product_works():
    global sugar
    coffee_name = coffee_order.get()
    temp_name = temp_order.get()
    size_name = size_order.get()
    sugar_name = radio_state.get()
    answer = menu_coffee.find_drink(coffee_name)
    coffee = coffee_maker.make_coffee(order=answer, heated=temp_name, asking_sugar=sugar_name, doubled=size_name)

    water_amount.config(text=f'{coffee_maker.resources["water"]} ml')
    milk_amount.config(text=f'{coffee_maker.resources["milk"]} ml')
    coffee_amount.config(text=f'{coffee_maker.resources["coffee"]} g')
    tea_amount.config(text=f'{coffee_maker.resources["tea_seeds"]} g')
    sugar_amount.config(text=f'{coffee_maker.resources["sugar"]} g')


    # print(coffee_maker.resources)
    result_coffee.config(text=coffee[0])
    result_coffee_2.config(text=coffee[1])
    print(money_machine.profit)
    if size_name == "Half":
        menu_coffee.find_drink(coffee_name).cost["Dollar"] = menu_coffee.find_drink(coffee_name).cost["Dollar"] * 2
        menu_coffee.find_drink(coffee_name).cost["Lira"] = menu_coffee.find_drink(coffee_name).cost["Lira"] * 2
        for ingredient in menu_coffee.find_drink(coffee_name).ingredients:
            menu_coffee.find_drink(coffee_name).ingredients[ingredient] = \
                menu_coffee.find_drink(coffee_name).ingredients[ingredient] * 2
    elif size_name == "Double":
        menu_coffee.find_drink(coffee_name).cost["Dollar"] = menu_coffee.find_drink(coffee_name).cost["Dollar"] / 2
        menu_coffee.find_drink(coffee_name).cost["Lira"] = menu_coffee.find_drink(coffee_name).cost["Lira"] / 2
        for ingredient in menu_coffee.find_drink(coffee_name).ingredients:
            menu_coffee.find_drink(coffee_name).ingredients[ingredient] = menu_coffee.find_drink(coffee_name).ingredients[ingredient] / 2

    if sugar_name == "without sugar".lower():
        answer.ingredients["sugar"] = sugar


#---------------------------------------------BUILD GUI-----------------------------------------#

window.title("Coffee Machine")
window.geometry("915x550")
window.config(bg="lightsalmon")

FONT_NAME = "Times"

choosing_coffee = Label(window, text="Choose Cofe:", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
choosing_coffee.grid(row=0, column=0, pady=20, padx=25, ipadx=5)

coffee_order = StringVar(window)
coffee_order.set(coffee_list[0])
coffee_order_show = OptionMenu(window, coffee_order, *coffee_list)
coffee_order_show.config(bg="lightsalmon", fg="black")
coffee_order_show.grid(row=0, column=1)

choosing_temp = Label(window, text="Choose cold or hot:", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
choosing_temp.grid(row=1, column=0, padx=20, ipadx=5)

temp_order = StringVar(window)
temp_order.set(temp_list[0])
temp_order_show = OptionMenu(window, temp_order, *temp_list)
temp_order_show.config(bg="lightsalmon", fg="black")
temp_order_show.grid(row=1, column=1)

choosing_size = Label(window, text="Choose size:", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
choosing_size.grid(row=2, column=0, padx=20, pady=25, ipadx=5)

size_order = StringVar(window)
size_order.set(size_list[2])
size_order_show = OptionMenu(window, size_order, *size_list)
size_order_show.config(bg="lightsalmon", fg="black")
size_order_show.grid(row=2, column=1)

radio_state = StringVar()
radio_button1 = Radiobutton(text="With sugar", value="with sugar", font=(FONT_NAME, 18, "bold"), variable=radio_state, bg="lightsalmon", fg="black")
radio_button2 = Radiobutton(text="Without sugar", value="without sugar", font=(FONT_NAME, 18, "bold"),  variable=radio_state, bg="lightsalmon", fg="black")
radio_button1.grid(row=3, column=0, padx=20)
radio_button2.grid(row=3, column=1, padx=20)

product_button = Button(window, text="Finish", highlightbackground="lightsalmon", highlightthickness=0, command=showing_parts)
product_button.grid(row=4, column=0, columnspan=2, pady=10)

payment = Label(window, text="Payment", font=(FONT_NAME, 25, "bold"), bg="lightsalmon", fg="black")
payment.grid(row=5, column=0, columnspan=2, pady=30)

choosing_currency = Label(window, text="Choose currency:", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
choosing_currency.grid(row=6, column=0)

currency_order = StringVar(window)
currency_order.set(currencies_list[0])
currency_order_show = OptionMenu(window, currency_order, *currencies_list)
currency_order_show.config(bg="lightsalmon", fg="black")
currency_order_show.grid(row=6, column=1)

enter_money_label = Label(window, text="Enter money:", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
enter_money_label.grid(row=7, column=0, pady=10)

enter_money = Entry(bg="white", fg="black", width=10)
enter_money.grid(row=7, column=1)

end_button = Button(window, text="Payment", highlightthickness=0, highlightbackground="lightsalmon", command=payment_fun)
end_button.grid(row=9, column=0, columnspan=2)

canvas = Canvas(width=280, height=285, bg="lightsalmon", highlightthickness=0)
coffee_machine_img = PhotoImage(file="coffeemachine.png")
canvas.create_image(136, 144, image=coffee_machine_img)
canvas.grid(column=2, row=0, rowspan=6)

result_coffee = Label(window, text="Here is your coffee....", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="brown")
result_coffee.grid(row=8, column=2)

result_coffee_2 = Label(window, text=" ", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="brown")
result_coffee_2.grid(row=9, column=2)

items_label = Label(window, text="Ingredients", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
items_label.grid(row=6, column=2)

payment_label = Label(window, text="Your change:", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
payment_label.grid(row=7, column=2)

water_resource = Label(window, text="Water", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
water_resource.grid(row=0, column=3)

water_amount = Label(window, text=f'{coffee_maker.resources["water"]} ml', font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
water_amount.grid(row=0, column=4)

milk_resource = Label(window, text="Milk", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
milk_resource.grid(row=1, column=3)

milk_amount = Label(window, text=f'{coffee_maker.resources["milk"]} ml', font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
milk_amount.grid(row=1, column=4)


coffee_resource = Label(window, text="Coffee seeds", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
coffee_resource.grid(row=2, column=3, padx=20)

coffee_amount = Label(window, text=f'{coffee_maker.resources["coffee"]} g', font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
coffee_amount.grid(row=2, column=4)

tea_resource = Label(window, text="Tea seeds", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
tea_resource.grid(row=3, column=3)

tea_amount = Label(window, text=f'{coffee_maker.resources["tea_seeds"]} g', font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
tea_amount.grid(row=3, column=4)

sugar_resource = Label(window, text="Sugar", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
sugar_resource.grid(row=4, column=3)

sugar_amount = Label(window, text=f'{coffee_maker.resources["sugar"]} g', font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
sugar_amount.grid(row=4, column=4)

order_resource = Label(window, text="Coffee ingredients", font=(FONT_NAME, 18, "bold"), bg="lightsalmon", fg="black")
order_resource.grid(row=5, column=3, columnspan=2)

order_water_milk_resource = Label(window, text="Water / Milk", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_water_milk_resource.grid(row=6, column=3)

order_water_milk_amount = Label(window,
                                text="0 ml / 0 ml",
                                font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_water_milk_amount.grid(row=6, column=4)

order_coffee_resource = Label(window, text="Coffee seeds", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_coffee_resource.grid(row=7, column=3)

order_coffee_amount = Label(window, text=f'0 g',
                            font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_coffee_amount.grid(row=7, column=4)

order_tea_resource = Label(window, text="Tea seeds", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_tea_resource.grid(row=8, column=3)

order_tea_amount = Label(window, text=f'0 g',
                         font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_tea_amount.grid(row=8, column=4)

order_sugar_resource = Label(window, text="Sugar", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_sugar_resource.grid(row=9, column=3)

order_sugar_amount = Label(window, text=f'0 g',
                           font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_sugar_amount.grid(row=9, column=4, pady=10)

order_cost_resource = Label(window, text="Price", font=(FONT_NAME, 15, "bold"), bg="lightsalmon", fg="black")
order_cost_resource.grid(row=10, column=3)

order_cost_amount = Label(window, text=f'0 $', font=(FONT_NAME, 15, "bold"),
                          bg="lightsalmon", fg="black")
order_cost_amount.grid(row=10, column=4)


window.mainloop()

